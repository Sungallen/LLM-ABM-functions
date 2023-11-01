import json
import numpy as np
import asyncio

from .classification import location_register as lr


a = [{'Activity': 'Morning Workout', 'Address': 'Home Gym', 'Time': '600', 'Transportation': 'Walk'},
     {'Activity': 'Breakfast and Family Time', 'Address': 'Home Kitchen',
         'Time': '710', 'Transportation': 'Walk'},
     {'Activity': 'Drive to Law Firm', 'Address': 'Baker & McKenzie Law Firm',
         'Time': '830', 'Transportation': 'Car'},
     {'Activity': 'Work', 'Address': 'Baker & McKenzie Law Firm',
         'Time': '900', 'Transportation': 'Walk'},
     {'Activity': 'Lunchtime', 'Address': 'Local Deli',
         'Time': '1230', 'Transportation': 'Walk'},
     {'Activity': 'Client Meetings', 'Address': 'Baker & McKenzie Law Firm',
         'Time': '1340', 'Transportation': 'Walk'},
     {'Activity': 'Drive Home', 'Address': 'Home',
         'Time': '1700', 'Transportation': 'Car'},
     {'Activity': 'Evening Prayers', 'Address': 'Home',
         'Time': '1800', 'Transportation': 'Walk'},
     {'Activity': 'Dinner with Family', 'Address': 'Home Kitchen',
         'Time': '1840', 'Transportation': 'Walk'},
     {'Activity': 'Family Leisure Time', 'Address': 'Home Living Room',
         'Time': '2000', 'Transportation': 'Walk'},
     {'Activity': 'Night Prayers', 'Address': 'Home',
         'Time': '2240', 'Transportation': 'Walk'},
     {'Activity': 'Sleep', 'Address': 'Home Bedroom', 'Time': '2300', 'Transportation': 'Walk'}]

b = [{'Activity': 'Morning Workout', 'Address': 'Accommodation', 'Time': '600', 'Transportation': 'Walk'},
     {'Activity': 'Breakfast and Family Time', 'Address': 'Accommodation',
         'Time': '710', 'Transportation': 'Walk'},
     {'Activity': 'Drive to Law Firm', 'Address': 'Commercial',
         'Time': '830', 'Transportation': 'Car'},
     {'Activity': 'Work', 'Address': 'Commercial',
         'Time': '900', 'Transportation': 'Walk'},
     {'Activity': 'Lunchtime', 'Address': 'Commercial',
         'Time': '1230', 'Transportation': 'Walk'},
     {'Activity': 'Client Meetings', 'Address': 'Commercial',
         'Time': '1340', 'Transportation': 'Walk'},
     {'Activity': 'Drive Home', 'Address': 'Accommodation',
         'Time': '1700', 'Transportation': 'Car'},
     {'Activity': 'Evening Prayers', 'Address': 'Accommodation',
         'Time': '1800', 'Transportation': 'Walk'},
     {'Activity': 'Dinner with Family', 'Address': 'Accommodation',
         'Time': '1840', 'Transportation': 'Walk'},
     {'Activity': 'Family Leisure Time', 'Address': 'Accommodation',
         'Time': '2000', 'Transportation': 'Walk'},
     {'Activity': 'Night Prayers', 'Address': 'Accommodation',
         'Time': '2240', 'Transportation': 'Walk'},
     {'Activity': 'Sleep', 'Address': 'Accommodation', 'Time': '2300', 'Transportation': 'Walk'}]


sem = asyncio.Semaphore(8)


async def test(sem: asyncio.Semaphore, input: str, category: str):
    async with sem:
        return lr().output(input=input, categoty=category)


async def test2(sem: asyncio.Semaphore, input: str):
    async with sem:
        return lr().output2(input=input)


async def start(schedule):
    task = [test(sem, f"Activity: {row['Activity']}",
                 row["Address"]) for row in schedule]
    results = await asyncio.gather(*task)
    print(results)
    return results


async def start2(schedule):
    task = [test2(
        sem, f"Activity: {row['Activity']} \r\r") for row in schedule]
    results = await asyncio.gather(*task)
    print(results)
    return results


if __name__ == "__main__":
    import time
    # print(" -=-=-=- -=-=-=- -=-=-=- -=-=-=- -=-=-=-")
    # start_time = time.time()
    # a = asyncio.run(start())

    # finish_time = time.time()
    # print(f"Total time: {finish_time - start_time}")
    # print(a)
    # print(" -=-=-=- -=-=-=- -=-=-=- -=-=-=- -=-=-=-")

    print(" -=-=-=- -=-=-=- -=-=-=- -=-=-=- -=-=-=-")
    start_time = time.time()
    a = asyncio.run(start2())

    finish_time = time.time()
    print(f"Total time: {finish_time - start_time}")
    print(a)
    print(" -=-=-=- -=-=-=- -=-=-=- -=-=-=- -=-=-=-")
