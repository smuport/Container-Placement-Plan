import random


# class state:
#     work_queues = [{'qc': 'QC1', 'containers': [{'id': 1, 'group': 'IF'}]}]
#     block_areas = [{'block': '1A', 'area': 2,
#                     'plans': [{'group': 'IF', 'bay': '1A16', 'capacity': 5},
#                             {"group": "OZ", "bay": "1C18", "capacity": 6}],
#                     'yc': {'name': 'YC1', 'location': 22},
#                     'instructions': [{'type': None, 'status': None, 'from': None, 'to': None, 'containerID': None}]},
#                     {"block": "1A", "area": 1,
#                     "plans": [{"group": "IF","bay": "1A02", "capacity": 0}],
#                     "yc": {"name": "YC1","location": 34},
#                     "instructions":[{'type': None, 'status': None, 'from': None, 'to': None, 'containerID': None}]}]
#
#
# containers = {'id': 1, 'group': 'OZ'}


def allocate(state, containers):
    try:
        cont_group = containers.get('group')
        reasonable_choice = []
        for block_area in state.block_areas:
            for plan in block_area['plans']:
                if cont_group == plan['group'] and plan['capacity'] > 0:
                    reasonable_choice.append(plan)
                if reasonable_choice:
                    my_choose = random.choice(reasonable_choice)
                    return my_choose,block_area
    except Exception as e:
        print('error',e)
# my_choose,block_area = allocate(state, containers)
# print('my_choose=',my_choose)
# print('block_area=',block_area)
