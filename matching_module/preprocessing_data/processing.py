import json
from shapely.geometry import Polygon, MultiPolygon
import os
from mysql_connect import *
working_directory = os.getcwd()
file_path = working_directory + \
    '/matching_module/preprocessing_data/back_bay.geojson'

with open(file_path, encoding='utf-8') as f:
    j = json.loads(f.read())


def to_polygons(listOfC: list):
    tmp = []
    for polygon in listOfC:
        tmp.append(Polygon(polygon))

    return tmp


building_category = {
    "Accommodation": ["apartments", "barracks", "bungalow", "cabin", "detached", "dormitory", "farm", "ger", "hotel", "house", "houseboat", "residential",
                      "semidetached_house", "static_caravan", "stilt_house", "terrace", "tree_house", "yes"],
    "Commercial": ["commercial", "industrial", "kiosk", "office", "retail", "supermarket", "warehouse"],
    "Religious": ["cathedral", "chapel", "church", "kingdom_hall", "monastery", "mosque", "presbytery", "religious", "shrine", "synagogue", "temple"],
    "Amenity": ["bakehouse", "bridge", "civic", "college", "fire_station", "government", "gatehouse", "hospital", "kindergarten", "museum", "public",
                "school", "toilets", "train_station", "transportation", "university", "static_railcar", ],
    "Agricultural": ["barn", "conservatory", "cowshed", "farm_auxiliary", "greenhouse", "slurry_tank", "stable", "sty", "livestock"],
    "Sports": ["grandstand", "pavilion", "riding_hall", "sports_hall", "stadium", "sports_centre"],
    "Storage": ["carport", "garage", "garages", "parking", "boathouse"],
    "Power": ["digester", "service", "transformer_tower", "water_tower", "storage_tank", "silo", "water_works"],
    "Other": ["beach_hut", "bunker", "castle", "construction", "container", "military", "roof", "ruins", "tent", "tower", "no", "shed", "canopy", ""],
}
# 9

# "Other": ["beach_hut ", "bunker ", "castle ", "construction ", "container ", "military ", "roof ", "ruins", "tent", "tower", "yes"],
keep_col = ["full_id", "osm_id", "osm_type", "building",
            "addr:city", "addr:housenumber", "addr:state", "addr:street",
            "tourism", "religion", "region", "government", "research",
            "military", "delivery"]

records = []
for row in j["features"]:
    row_record = []
    for i, key in enumerate(row["properties"]):

        if key in keep_col:
            row_record.append(row["properties"][key])
            # print(f'{i:3d} >< {key} >> {row["properties"][key]}')
            if key == "building":
                for bu_ca in building_category:
                    if row["properties"][key] in building_category[bu_ca]:
                        # print(bu_ca)
                        row_record.append(bu_ca)
                        # print(row_record)
                        break
    for i in range(3):
        row_record.append('')
    multi = MultiPolygon(to_polygons(row['geometry']['coordinates'][0]))
    # print([multi.centroid.x, multi.centroid.y])
    # row_record.append([multi.centroid.x, multi.centroid.y])
    row_record.append(str(multi.centroid.x))
    row_record.append(str(multi.centroid.y))
    if type(multi.centroid.x) == str | type(multi.centroid.y) == str:
        print(1232131231312318937127891739827898)
    # print(row_record)
    if len(row_record) != 18:
        print(row_record, len(row_record))
        print('error')
    # if len(row_record) != 17:
    #     print(row_record)
    print(row_record)
    records.append(row_record)
# print(records)
# print(len(records[0]))
# print(records[0])
# print(records[1])
# print(records[2])

_sql = '''
    INSERT IGNORE back_bay_buildings(full_id, osm_id, osm_type, building, building_category, 
                            addr_city, addr_housenumber, addr_state, addr_street,
                            tourism, religion, region, government,
                            research, military, delivery, lng, lat)
                        VALUES(%s,%s,%s,%s,%s
                            ,%s,%s,%s,%s
                            ,%s,%s,%s,%s
                            ,%s,%s,%s,%s,%s)
'''

Sql_Execute_Many(_sql, records)
