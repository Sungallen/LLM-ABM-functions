import networkx as nx
import osmnx as ox
import taxicab as tc
import geopandas as gpd
import json
import time


# Define the location
location = "Cambridge, MA, USA"

# Download the street network
graph = ox.graph_from_place(location, network_type='drive')

# Convert the graph to GeoDataFrames
nodes, edges = ox.graph_to_gdfs(graph)

# Convert the GeoDataFrame to GeoJSON
geojson = json.loads(edges.to_json())


def shortest_path_algorithm(schedule_route):
    updated_schedule_route = []
    for index, i in enumerate(schedule_route):
        updated_schedule_route.append(schedule_route[index])
        if index + 1 != len(schedule_route):
            origl = ox.nearest_nodes(
                graph, schedule_route[index]['log'], schedule_route[index]['lat'])
            dest = ox.nearest_nodes(
                graph, schedule_route[index + 1]['log'], schedule_route[index + 1]['lat'])
            print(origl, dest)
            route = nx.shortest_path(graph, origl, dest, weight='travel_time')
            print('length', len(route))
            if len(route) == 1:
                continue
            time_interval = (
                schedule_route[index + 1]['Time'] - i['Time']) / (len(route) + 1)
            time_interval_index = 1
            for j, node in nodes.loc[route].iterrows():
                temp_json = {}
                temp_json['Time'] = i['Time'] + \
                    time_interval * time_interval_index
                temp_json['log'] = node.x
                temp_json['lat'] = node.y
                temp_json['Activity'] = i['Activity']
                temp_json['Address'] = i['Address']
                temp_json['Transportation'] = i['Transportation']
                time_interval_index += 1
                updated_schedule_route.append(temp_json)
    return updated_schedule_route
