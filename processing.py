import json
from shortest_path.index import shortest_path_algorithm

# array = []
# with open('agent_behavior_in_cambridge_changed.json', 'r') as file:
#     data = json.load(file)

#     for i in data:
#         element = {}
#         path = []
#         timestamp = []
#         for j in i['Activities']:
#             path.append([j['log'], j['lat']])
#             timestamp.append(j['Time'])
#         element['path'] = path
#         element['timestamp'] = timestamp
#         array.append(element)

# with open('path_array_changed', 'w+') as output:
#     json.dump(array, output)

with open('path_array_changed.json', 'r') as file:
    data = json.load(file)
    color_codes = [[89, 17, 247], [0, 255, 206], [255, 42, 109]]
    for i in range(len(data)):
        data[i]['color'] = color_codes[i % 3]
    with open('path_array_new_changed.json', 'w') as output:
        json.dump(data, output)
