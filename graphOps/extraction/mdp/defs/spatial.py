import shapely
from pyproj import Geod


# Makes pairs of coordinates from a list of coordinates.  ll: A list of coordinates.
# Returns:  A list of pairs of coordinates.
def make_pairs(ll):
    coords = []
    for i in range(0, len(ll), 2):
        coords.append((ll[i], ll[i + 1]))

    return coords


def gj(geom, value):
    if geom == None:
        return None
    test = geom.split()
    test = [float(x) for x in test]
    if len(test) < 2:
        return None

    cp = make_pairs(test)

    if len(cp) == 1:
        # print("POINT")
        geom = shapely.Point(cp)
    elif len(cp) == 2:
        # print("BOX") #  this is a box, which isn't in WKT, so make a polygon from
        # any two items pairs.  The issue here is that it could also be a line,
        # so we need to pass the predicate from the graph to know
        min_lat, min_lon = cp[0][0], cp[0][1]  # from schema.org we get LAT LONG,
        max_lat, max_lon = cp[1][0], cp[1][1]

        geom = shapely.box(min_lon, min_lat, max_lon, max_lat) # for Shapely, present these as LONG LAT
    else:
        # print("POLYGON")
        geom = shapely.Polygon(cp)

    if value == "centroid":
        return geom.centroid
    elif value == "length":
        return geom.length
    elif value == "area":
        geod = Geod(ellps="WGS84")
        area = abs(geod.geometry_area_perimeter(geom)[0])
        return area
    elif value == "wkt":
        return shapely.to_wkt(geom)
    elif value == "geojson":
        return shapely.to_geojson(geom)
    else:
        return None
