import random


# class state:
#     work_queues = [{'qc': 'QC1', 'containers': [{'id': 1, 'group': 'IF'}]}]
#     block_areas = [{'block': '1A', 'area': 2,
#                     'plans': [{'group': 'IF', 'bay': '1A16', 'capacity': 0},
#                             {"group": "OZ", "bay": "1C18", "capacity": 0}],
#                     'yc': {'name': 'YC1', 'location': 22},
#                     'instructions': [{'type': None, 'status': None, 'from': None, 'to': None, 'containerID': None}]},
#                     {"block": "1A", "area": 1,
#                     "plans": [{"group": "IF","bay": "1A02", "capacity": 0}],
#                     "yc": {"name": "YC1","location": 34},
#                     "instructions":[{'type': None, 'status': None, 'from': None, 'to': None, 'containerID': None}]}]
#
#
# containers = [{'id': 1, 'group': 'OZ'}]


def allocate(state, containers):
    result=[]
    # for container in containers.containers:
    cont_id = containers['id']
    cont_group = containers['group']

    reasonable_choice = []
    allocated_contID = []

    for block_area in state.block_areas:

        for plan in block_area['plans']:
            bay = plan['bay']

            for instruction in block_area['instructions']:
                allocated_container_id = instruction['containerID']
                allocated_contID.append(allocated_container_id)

                if cont_id in allocated_contID:
                    print(f" {cont_id}重复分配，停止。")
                    break

                else:
                    # for block_area in state.block_areas:
                    #
                    #     for plan in block_area['plans']:
                            #P = plan


                            if cont_group == plan['group'] and plan['capacity'] > 0:
                                reasonable_choice.append(block_area)
                                #R=reasonable_choice

                                my_choose = random.choice(reasonable_choice)
                                for choose_plan in my_choose['plans']:
                                    if choose_plan['group'] == cont_group:
                                        choose_plan['capacity'] -= 1
                                        break

                                my_choose['instructions'][0]['type']= 'U'
                                my_choose['instructions'][0]['status']= '已配车'
                                my_choose['instructions'][0]['to']= choose_plan['bay']
                                my_choose['instructions'][0]['containerID']= cont_id
                                a = choose_plan['group']
                                b = choose_plan['bay']
                                c = choose_plan['capacity']


                                index = state.block_areas.index(my_choose)
                                state.block_areas[index] = my_choose

                            if not reasonable_choice:
                                continue
                            # print(my_choose)
                            # print(choose_plan)
                            return my_choose

# print(allocate(state, containers))
