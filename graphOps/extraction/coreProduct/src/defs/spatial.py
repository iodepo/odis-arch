import shapely
from pyproj import Geod


def make_pairs(ll):
    """Makes pairs of coordinates from a list of coordinates.

    Args:
      ll: A list of coordinates.

    Returns:
      A list of pairs of coordinates.
    """

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
        # print("BOX")
        geom = shapely.box(cp[0][0], cp[0][1], cp[1][0], cp[1][1])
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
