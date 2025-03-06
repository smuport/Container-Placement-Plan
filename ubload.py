import random


class state:
    work_queues = [{'qc': 'QC1', 'containers': [{'id': 1, 'group': 'IF'}]}]
    block_areas = [{'block': '1A', 'area': 2,
                    'plans': [{'group': 'IF', 'bay': '1A16', 'capacity': 21}],
                    'yc': {'name': 'YC1', 'location': 22},
                    'instructions': [{'type': None, 'status': None, 'from': None, 'to': None, 'containerID': None}]}]


class containers:
    containers = [{'id': 1, 'group': 'IF'}]


def allocate(state, containers):
    for container in containers.containers:
        cont_id = container['id']
        cont_group = container['group']

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
                    for block_area in state.block_areas:

                        for plan in block_area['plans']:

                            if cont_group == plan['group'] and plan['capacity'] > 0:
                                reasonable_choice.append(block_area)
                                my_choose = random.choice(reasonable_choice)
                                my_choose['plans'][0]['capacity'] -= 1
                                my_choose['instructions'][0]['type']= 'U'
                                my_choose['instructions'][0]['status']= '已配车'
                                my_choose['instructions'][0]['to']= bay
                                my_choose['instructions'][0]['containerID']= cont_id
                                a = my_choose['plans'][0]['group']
                                b = my_choose['plans'][0]['bay']
                                c = my_choose['plans'][0]['capacity']


                                index = state.block_areas.index(my_choose)
                                state.block_areas[index] = my_choose

                            if not reasonable_choice:
                                continue
                            print(my_choose)
                            return {f'group:{a}, bay:{b}, capacity:{c}'}

allocate(state, containers)