import random
from classification import state


# 测试数据
# class state:
#     work_queues = [{'qc': 'QC1', 'containers': [{'id': 1, 'group': 'IF'}]}]
#     block_areas = [{'block': '1A', 'area': 2,
#                     'plans': [{'group': 'IF', 'bay': '1A16', 'capacity': 21}],
#                     'yc': {'name': 'YC1', 'location': 22},
#                     'instructions': [{'type': None, 'status': None, 'from': None, 'to': None, 'containerID': None}]}]
#
#
# class containers:
#     containers = [{'id': 1, 'group': 'IF'}]


def allocate(state, containers):
    result = []

    cont_id = containers['id']
    cont_group = containers['group']
    # print(cont_id, cont_group)
    reasonable_choice = []
    allocated_contID = []

    for block_area in state.block_areas:

        for plan in block_area['plans']:
            bay = plan['bay']

            for instruction in block_area['instructions']:
                allocated_container_id = instruction['containerID']
                allocated_contID.append(allocated_container_id)

            if cont_id in allocated_contID:
                # print(f" {cont_id}重复分配，停止。")
                break

            else:
                # for block_area in state.block_areas:
                #
                #     for plan in block_area['plans']:

                        if cont_group == plan['group'] and plan['capacity'] > 0:
                            reasonable_choice.append(block_area)
                            my_choose = random.choice(reasonable_choice)
                            my_choose['plans'][0]['capacity'] -= 1
                            my_choose['instructions'][0]['type'] = 'U'
                            my_choose['instructions'][0]['status'] = '已配车'
                            my_choose['instructions'][0]['to'] = bay
                            my_choose['instructions'][0]['containerID'] = cont_id
                            # a = my_choose['plans'][0]['group']
                            # b = my_choose['plans'][0]['bay']
                            # c = my_choose['plans'][0]['capacity']

                            index = state.block_areas.index(my_choose)
                            state.block_areas[index] = my_choose
                            # Return result in expected format
                            # Ensure instructions array has at least one element
                            if not my_choose['instructions']:
                                my_choose['instructions'].append({
                                    'type': 'U',
                                    'status': '已配车',
                                    'to': bay,
                                    'containerID': cont_id
                                })
                            
                            result = {
                                'block': my_choose['block'],
                                'area': my_choose['area'],
                                'plans': my_choose['plans'],
                                'yc': my_choose['yc'],
                                'instructions': my_choose['instructions']
                            }
                            return result
                        if not reasonable_choice:
                            continue

    # Return empty dict if no allocation found
    return {
        'block': None,
        'area': None,
        'plans': [],
        'yc': None,
        'instructions': [{
            'type': None,
            'status': None,
            'to': None,
            'containerID': None
        }]
    }


# a = allocate(state, {'id': 120, 'group': 'IZ'})
# print(a)
