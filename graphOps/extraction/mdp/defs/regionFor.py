from . import datashaping
import shapely.geometry
import os, json, re

import shapely.wkt
import shapely.geometry
from urllib.request import urlopen

with open(os.path.join(os.path.dirname(__file__), 'regions-clipped.geojson'), 'r') as f:
    geo_regions = json.load(f)['features']
    for r in geo_regions:
        r['shape'] = shapely.geometry.shape(r['geometry'])

# leverage the UNSD API "GeoArea" JSON endpoint, instead of locally-stored CSV
#  see https://unstats.un.org/SDGAPI/swagger/
unsdGeoareaEndpoint = "https://unstats.un.org/SDGAPI/v1/sdg/GeoArea/Tree"
response = urlopen(unsdGeoareaEndpoint)
unsdDataJSON = json.loads(response.read())

# use the "World (total) by continental regions" branch
continentalRegions = unsdDataJSON[1]
continentalRegionsChildren = continentalRegions['children']

# parse the JSON from the API call
countries_dict_with_regions = {}
country_map_list = []

for list_regions in continentalRegionsChildren:
    if list_regions['children'] == None:
        regionName = list_regions['geoAreaName']
        # print('Region name (no children): ' + regionName)
    else:
        regionName = list_regions['geoAreaName']
        # print('Region name: ' + regionName)
        # loop through sub-regions
        for list_subregions in list_regions['children']:
            subRegionName = list_subregions['geoAreaName']
            # print('Sub-region name: ' + subRegionName)
            # loop through intermediate region items
            for list_intermediate_regions in list_subregions['children']:
                if list_intermediate_regions['type'] == 'Region':
                    intermediateRegionName = list_intermediate_regions['geoAreaName']
                    # print('Intermediate region name: ' + intermediateRegionName)
                    # loop through intermediate region children
                    for list_intermediate_region_children in list_intermediate_regions['children']:
                        countryName = list_intermediate_region_children['geoAreaName'].lower()
                        # print('Country name: ' + countryName)
                        countries_dict_with_regions[countryName] = [regionName, subRegionName]
                        country_map_list.append((datashaping.normalize(countryName), countryName))
                else:
                    countryName = list_intermediate_regions['geoAreaName'].lower()
                    # print('Country name: ' + countryName)
                    countries_dict_with_regions[countryName] = [regionName, subRegionName]
                    country_map_list.append((datashaping.normalize(countryName), countryName))


def mergeRegions(df):
    df['region'] = df[['nregion', 'aregion','cregion', 'fregion']].apply(lambda x: list(set(x[0] + x[1] + x[2]+ x[3])), axis=1)
    del df['nregion']
    del df['aregion']
    del df['cregion']
    del df['fregion']
    return df

def normalize(s):
    if isinstance(s, str):
      s = s.lower()
      s = re.sub(r"\(.*\)","",s)
      s = re.sub(r"\[.*\]","",s)
      s = re.sub(r"and|the|of","", s)
      s = s.rstrip('.')
      return set(s.split(None))
    else:
      return set(s)

def address(address):
    normalized = normalize(address)
    value = list()
    for parts, country in country_map_list:
        if parts <= normalized:
          if country in countries_dict_with_regions:
            value = countries_dict_with_regions[country]
    return value

def name(n):
    normalized = normalize(n)
    value = list()
    for parts, country in country_map_list:
      if parts <= normalized:
        if country in countries_dict_with_regions:
          value = countries_dict_with_regions[country]
    return value


def countryLastProcessing(countryOfLastProcessing):
    normalized = normalize(countryOfLastProcessing)
    value = list()
    for parts, country in country_map_list:
        if parts <= normalized:
          if country in countries_dict_with_regions:
            value = countries_dict_with_regions[country]
    return value

def feature(feature):
    try:
        the_geom = shapely.wkt.loads(feature)
        return [r['properties']['name'] for r in geo_regions if r['shape'].intersects(the_geom)]
    except:
        return list()
