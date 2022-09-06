import geopandas as gdp
from classes import SimpleNode, SimpleArc
import json

shp = gdp.read_file("vertices_height_split.shp")
geometry_list = []
node_list = []
node_list_json = {"feature_types": "POINT",
                  "EPSG": "EPSG:3006",
                  "features": []}
arc_list_json = {"feature_types": "LINE",
                  "EPSG": "EPSG:3006",
                  "features": []}

i = 0
for row in shp.iterrows():
    if row[1].geometry in geometry_list:
        ind = geometry_list.index(row[1].geometry)
        exist_node = node_list[ind]
        exist_node.add_arcs_id(row[1]['ORIG_FID'])
    else:
        node = SimpleNode(i)
        node.set_xy([row[1].geometry.coords.xy[0][0], row[1].geometry.coords.xy[1][0]])
        node.add_arcs_id(row[1]['ORIG_FID'])
        node.set_height(row[1]['RASTERVALU'])
        node_list.append(node)
        node_list_json['features'].append(node.print_me_as_json())
        geometry_list.append(row[1].geometry)
        i += 1

arc_list = []
arc_id_list = []
for node in node_list:
    for arc_id in node.arc_list:
        if arc_id not in arc_id_list:
            arc = SimpleArc(arc_id)
            arc.process_arc(node, node_list)
            arc_id_list.append(arc_id)
            arc_list.append(arc)
            arc_list_json['features'].append(arc.print_me_as_json())

json_data_node = json.dumps(node_list_json)
json_data_arc = json.dumps(arc_list_json)

with open("node_json.json", "w") as data:
    data.write(json_data_node)

with open("arc_json.json", "w") as data:
    data.write(json_data_arc)
