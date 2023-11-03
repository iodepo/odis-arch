import os
import json
import re
import shapely
import shapely.wkt
import shapely.geometry
from urllib.request import urlopen

from defs import regionFor

with open(os.path.join(os.path.dirname(__file__),'regions-clipped.geojson'), 'r') as f:
    geo_regions = json.load(f)['features']
    for r in geo_regions:
        r['shape'] = shapely.geometry.shape(r['geometry'])

#leverage the UNSD API "GeoArea" JSON endpoint, instead of locally-stored CSV
#  see https://unstats.un.org/SDGAPI/swagger/
unsdGeoareaEndpoint = "https://unstats.un.org/SDGAPI/v1/sdg/GeoArea/Tree"
response = urlopen(unsdGeoareaEndpoint)
unsdDataJSON = json.loads(response.read())
#use the "World (total) by continental regions" branch
continentalRegions = unsdDataJSON[1]
continentalRegionsChildren = continentalRegions['children']

#parse the JSON from the API call
countries_dict_with_regions = {}
country_map_list = []

for list_regions in continentalRegionsChildren:
    if list_regions['children'] == None:
        regionName = list_regions['geoAreaName']
        #print('Region name (no children): ' + regionName)
    else:
        regionName = list_regions['geoAreaName']    
        #print('Region name: ' + regionName)
        #loop through sub-regions
        for list_subregions in list_regions['children']:
            subRegionName = list_subregions['geoAreaName']
            #print('Sub-region name: ' + subRegionName)            
            #loop through intermediate region items
            for list_intermediate_regions in list_subregions['children']:
                if list_intermediate_regions['type'] == 'Region':
                    intermediateRegionName = list_intermediate_regions['geoAreaName']
                    #print('Intermediate region name: ' + intermediateRegionName)
                    #loop through intermediate region children
                    for list_intermediate_region_children in list_intermediate_regions['children']:
                        countryName = list_intermediate_region_children['geoAreaName'].lower()
                        #print('Country name: ' + countryName)
                        countries_dict_with_regions[countryName] = [regionName, subRegionName] 
                        country_map_list.append((normalize(countryName), countryName))
                else:
                    countryName = list_intermediate_regions['geoAreaName'].lower()
                    #print('Country name: ' + countryName)                   
                    countries_dict_with_regions[countryName] = [regionName, subRegionName]                 
                    country_map_list.append((normalize(countryName), countryName))
                    
#print(countries_dict_with_regions)
#print(country_map_list)

if __name__ == '__main__':

    print('regionsForFeature tests...')
    for feature in (
            'POLYGON ((-95.5 19.5,-95.5 31.5,-73.5 31.5,-73.5 19.5,-95.5 19.5))',
            'POLYGON ((144.401499 13.11742,144.401499 15.622688,145.8872 15.622688,145.8872 13.11742,144.401499 13.11742))',
            'POINT (0 0)',
            'POINT (-9 53)'
            ):
        print('    ',regionFor.regionsForFeature(feature))
        
    print('regionForAddress tests...')
    for address in (
            'IOC Science and Communication Centre on Harmful Algae, University of Copenhagen - University of Copenhagen, Department of Biology - DK-1353 K\u00f8benhavn K - Denmark',
            'P. O. BOX LG 99 Legon-Accra, Ghana.',
            ):
        print('    ',regionFor.regionForAddress(address))
        
    print('regionForName tests...')    
    for name in (
            "Marine Science Country Profiles : Kenya",
            "The fisheries of Barbados and some of their problems",
            "Fiji : Where's the data?"
            ):
        print('    ',regionFor.regionForName(name))
        
    print('regionForCountryOfLastProcessing tests...')    
    for countryOfLastProcessing in (
            'Angola',
            'Panama',
            'Fiji'
            ):
        print('    ',regionFor.regionForCountryOfLastProcessing(countryOfLastProcessing))
