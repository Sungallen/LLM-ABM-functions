from .mysql.utilities import Sql_Fetch_All
import random


def buildings_selection(schedule_types):
    accommodation_sql = '''
                       select * 
                        from buildings
                        where lng <= -71.06639 and lng >= -71.11767 
                        and lat <= 42.37602 and lat >= 42.35208 
                        and building_category = 'Accommodation';
                        '''
    accommodation_list = Sql_Fetch_All(accommodation_sql)
    choice_accommodation = accommodation_list[random.randint(
        0, len(accommodation_list) - 1)]
    # print(choice_accommodation[17])
    positions_list = []
    for i in schedule_types:
        if i == 'Accommodation':
            positions_list.append(
                [choice_accommodation[16], choice_accommodation[17]])
            continue
        print(i)
        select_building_sql = f'''
                         select * 
                        from buildings
                        where lng <= -71.06639 and lng >= -71.11767 
                        and lat <= 42.37602 and lat >= 42.35208 
                        and building_category = '{i}';
                        '''
        selected_buildings = Sql_Fetch_All(select_building_sql)
        if len(selected_buildings) == 0:
            positions_list.append(
                [choice_accommodation[16], choice_accommodation[17]])
            continue
        choice_building = selected_buildings[random.randint(
            0, len(selected_buildings) - 1)]
        # print(choice_building)
        positions_list.append([choice_building[16], choice_building[17]])
    return positions_list


# buildings_selection(['Sports', 'Accommodation', 'Accommodation', 'Commercial',
#                     'Accommodation', 'Commercial', 'Accommodation', 'Accommodation', 'Accommodation'])
