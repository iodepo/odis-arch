import normalize
import shapely.geometry

def regionForAddress(address):
    normalized = normalize(address)
    for parts, country in country_map_list:
        if parts <= normalized:
            return countries_dict_with_regions[country]

def regionForName(name):
    normalized = normalize(name)
    for parts, country in country_map_list:
        if parts <= normalized:
            return countries_dict_with_regions[country]

def regionForCountryOfLastProcessing(countryOfLastProcessing):
    normalized = normalize(countryOfLastProcessing)
    for parts, country in country_map_list:
        if parts <= normalized:
            return countries_dict_with_regions[country]

def regionsForFeature(feature):
    the_geom= shapely.wkt.loads(feature)
    return [r['properties']['name'] for r in geo_regions if r['shape'].intersects(the_geom)]
