import asyncio
from matching_module.main import start, start2
from schedule_generator.index import Agent
from buildings_selection.index import buildings_selection
from shortest_path.index import shortest_path_algorithm
import json


async def main():
    print(213)
    # x = Agent("")
    # x._generate()
    # print(x.person)
    # schedule = call(x.person)

    # generate agent itineraries
    # schedule_routes = []
    # for i in range(5):
    #     print(i)
    #     x = Agent("")
    #     x._generate()
    #     schedule = call(x.person)
    #     x.person['Activities'] = schedule
    #     schedule_routes.append(x.person)
    # with open('new.json', 'w+') as output:
    #     json.dump(schedule_routes, output)
    x = Agent("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")
    person = x._generate()
    # print(person['schedule'])
    a = await start2(person['schedule'])
    positions_list = buildings_selection(a)
    print(positions_list)
    for index, value in enumerate(person['schedule']):
        person['schedule'][index]['Start time'] = int(
            person['schedule'][index]['Start time'])
        person['schedule'][index]['End time'] = int(
            person['schedule'][index]['End time'])
        person['schedule'][index]['log'] = float(positions_list[index][0])
        person['schedule'][index]['lat'] = float(positions_list[index][1])
    print(person['schedule'])
    # matching algorithm
    # with open('agents_behavor_in_cambridge_2.json', 'r') as file:
    #     data = json.load(file)
    #     for i in data:
    #         a = await start2(i['Activities'])
    #         positions_list = buildings_selection(a)
    #         print(positions_list)
    #         for index, value in enumerate(i['Activities']):
    #             i['Activities'][index]['Time'] = int(
    #                 i['Activities'][index]['Time'])
    #             i['Activities'][index]['log'] = float(positions_list[index][0])
    #             i['Activities'][index]['lat'] = float(positions_list[index][1])
    #         schedule_route = shortest_path_algorithm(i['Activities'])
    #         i['Activities'] = schedule_route
    #     with open('agent_behavior_in_cambridge_changed', 'w+') as output:
    #         json.dump(data, output)

    # with open('agents_behavor_in_cambridge.json', 'w+') as output:
    #     json.dump(schedule_routes, output)
    #     # generate 4 7
    #     agent_itineraries = []
    #     schedule = call(agent_profiles[3])
    #     a = await start2(schedule)
    #     positions_list = buildings_selection(a)
    #     for index, value in enumerate(schedule):
    #         schedule[index]['Time'] = int(schedule[index]['Time'])
    #         schedule[index]['log'] = float(positions_list[index][0])
    #         schedule[index]['lat'] = float(positions_list[index][1])
    #    # schedule_route = shortest_path_algorithm(schedule)
    #     agent4 = agent_profiles[3]
    #     agent4['Activities'] = schedule
    #     agent_itineraries.append(agent4)

    #     schedule = call(agent_profiles[6])
    #     a = await start2(schedule)
    #     positions_list = buildings_selection(a)
    #     for index, value in enumerate(schedule):
    #         schedule[index]['Time'] = int(schedule[index]['Time'])
    #         schedule[index]['log'] = float(positions_list[index][0])
    #         schedule[index]['lat'] = float(positions_list[index][1])
    #    # schedule_route = shortest_path_algorithm(schedule)
    #     agent6 = agent_profiles[6]
    #     agent6['Activities'] = schedule
    #     agent_itineraries.append(agent6)

    #     with open("agents_itineraries.json", 'w') as output:
    #         json.dump(agent_itineraries, output)
    #     print('++++++++++++++++++++++++++++++')
    #     print(a)
    # with open('agents_itineraries.json', 'r') as file:
    #     data = json.load(file)
    #     print(data)
    #     a = await start2(data[0]["Activities"])
    #     b = await start2(data[1]["Activities"])

    #     positions_list = buildings_selection(a)
    #     for index, value in enumerate(data[0]["Activities"]):
    #         data[0]["Activities"][index]['Time'] = int(
    #             data[0]["Activities"][index]['Time'])
    #         data[0]["Activities"][index]['log'] = float(
    #             positions_list[index][0])
    #         data[0]["Activities"][index]['lat'] = float(
    #             positions_list[index][1])
    #     positions_list = buildings_selection(b)
    #     for index, value in enumerate(data[1]["Activities"]):
    #         data[1]["Activities"][index]['Time'] = int(
    #             data[1]["Activities"][index]['Time'])
    #         data[1]["Activities"][index]['log'] = float(
    #             positions_list[index][0])
    #         data[1]["Activities"][index]['lat'] = float(
    #             positions_list[index][1])

    #     with open('back_bay_itineraries.json', 'w') as output:
    #         json.dump(data, output)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
