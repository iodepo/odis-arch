from . import datashaping
import shapely.geometry
import os, json

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


def address(address):
    normalized = datashaping.normalize(address)
    for parts, country in country_map_list:
        if parts <= normalized:
            return countries_dict_with_regions[country]

def name(name):
    normalized = datashaping.normalize(name)
    for parts, country in country_map_list:
        if parts <= normalized:
            return countries_dict_with_regions[country]

def countryLastProcessing(countryOfLastProcessing):
    normalized = datashaping.normalize(countryOfLastProcessing)
    for parts, country in country_map_list:
        if parts <= normalized:
            return countries_dict_with_regions[country]

def feature(feature):
    the_geom= shapely.wkt.loads(feature)
    return [r['properties']['name'] for r in geo_regions if r['shape'].intersects(the_geom)]
