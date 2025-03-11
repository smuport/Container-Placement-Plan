# # # """
# # # 实际在event中的result应该是一条一条的 在这边为了先测试输出的环节 人为简化了result并设置了测试数据
# # # """
import random

#
# results = [
#     {'block': '1A', 'area': 2, 'instructions': [{'to': '1A16', 'containerID': 7}]},
#     {'block': '1D', 'area': 2, 'instructions': [{'to': '1D16', 'containerID': 1}]},
#     {'block': '1C', 'area': 1, 'instructions': [{'to': '1C16', 'containerID': 2}]},
#     {'block': '1A', 'area': 2, 'instructions': [{'to': '1A16', 'containerID': 3}]},
#     {'block': '1B', 'area': 2, 'instructions': [{'to': '1B16', 'containerID': 4}]},
#     {'block': '1C', 'area': 2, 'instructions': [{'to': '1C16', 'containerID': 5}]},
#     {'block': '1D', 'area': 2, 'instructions': [{'to': '1D16', 'containerID': 6}]},
#     {'block': '1A', 'area': 2, 'instructions': [{'to': '1A16', 'containerID': 11}]}
# ]
# 假设塞入统一贝位
results = [
    {'block': '1A', 'area': 2, 'instructions': [{'to': '1A16', 'containerID': 7}]},
    {'block': '1A', 'area': 2, 'instructions': [{'to': '1A16', 'containerID': 1}]},
    {'block': '1A', 'area': 2, 'instructions': [{'to': '1A16', 'containerID': 2}]},
    {'block': '1A', 'area': 2, 'instructions': [{'to': '1A16', 'containerID': 3}]},
    {'block': '1A', 'area': 2, 'instructions': [{'to': '1A16', 'containerID': 4}]},
    {'block': '1A', 'area': 2, 'instructions': [{'to': '1A16', 'containerID': 5}]},
    {'block': '1A', 'area': 2, 'instructions': [{'to': '1A16', 'containerID': 6}]},
    {'block': '1A', 'area': 2, 'instructions': [{'to': '1A16', 'containerID': 11}]}
]


#
#
def test(results):
    global result, plan
    task_dict = {'Aplan': {'task_list': [], 'arrive_time': [], 'finish_time': []},
                 'Bplan': {'task_list': [], 'arrive_time': [], 'finish_time': []},
                 'C1plan': {'task_list': [], 'arrive_time': [], 'finish_time': []},
                 'C2plan': {'task_list': [], 'arrive_time': [], 'finish_time': []},
                 'Dplan': {'task_list': [], 'arrive_time': [], 'finish_time': []}}
    for i in range(len(results)):
        result = results[i]
        unload_time = random.randint(10000, 10010)
        container_id = result['instructions'][0]['containerID']
        result_block = result['block']
        result_area = result['area']
        valid = {
            '1A': 'Aplan',
            '1B': 'Bplan',
            '1C': {'1': 'C1plan', '2': 'C2plan'},
            '1D': 'Dplan'
        }
        for i in valid:
            if i == result_block:
                if i == '1C':
                    if result_area == 1:
                        plan = valid[i].get('1')
                    elif result_area == 2:
                        plan = valid[i].get('2')
                else:
                    plan = valid[i]
        print(plan)
        tasklist = task_dict[plan].get('task_list')
        tasklist.append(container_id)
        task_dict[plan]['arrive_time'].append(unload_time + 3)
    # #         # if result_block == '1A':
    # #         #     task_dict['Aplan']['task_list'].append(container_id)
    # #         #     task_dict['Aplan']['arrive_time'].append(unload_time + 3)
    # #         # elif result_block == '1B':
    # #         #     task_dict['Bplan']['task_list'].append(container_id)
    # #         #     task_dict['Bplan']['arrive_time'].append(unload_time + 3)
    # #         # elif result_block == '1C':
    # #         #     if result_area == 1:
    # #         #         task_dict['C1plan']['task_list'].append(container_id)
    # #         #         task_dict['C1plan']['arrive_time'].append(unload_time + 3)
    # #         #     elif result_area == 2:
    # #         #         task_dict['C2plan']['task_list'].append(container_id)
    # #         #         task_dict['C2plan']['arrive_time'].append(unload_time + 3)
    # #         # elif result_block == '1D':
    # #         #     task_dict['Dplan']['task_list'].append(container_id)
    # #         #     task_dict['Dplan']['arrive_time'].append(unload_time + 3)
    print(task_dict)
    caculateWaitTime(task_dict)
    # # #
    # # #
    # # # """
    # # # 演示一下代码取出来的信息
    for plan_name in task_dict:
        plan_info = task_dict[plan_name]
        print(f"{plan_name}: f{plan_info}")


# Aplan: f{'task_list': [7, 3, 11], 'arrive_time': [9, 3, 11], 'finish_time': []}
# Bplan: f{'task_list': [4], 'arrive_time': [11], 'finish_time': []}
# C1plan: f{'task_list': [2], 'arrive_time': [12], 'finish_time': []}
# C2plan: f{'task_list': [5], 'arrive_time': [12], 'finish_time': []}
# Dplan: f{'task_list': [1, 6], 'arrive_time': [12, 8], 'finish_time': []}

# # # """
# # #
# # #
def caculateWaitTime(task_dict):
    for plan_name in task_dict:
        plan_info = task_dict[plan_name]
        for i in range(len(plan_info['task_list'])):
            if i == 0:
                wait_time = 0
            elif i != 0:
                finsih_time = plan_info['finish_time']
                arrive_time = plan_info['arrive_time']
                if finsih_time[i - 1] < arrive_time[i]:
                    wait_time = finsih_time[i - 1] - arrive_time[i]
                else:
                    wait_time = 0
            return wait_time

test(results)
# # #
# # #
# # # test(results)
# # class state:
# #     work_queues = [{'qc': 'QC1', 'containers': [{'id': 1, 'group': 'IF'}]},
# #                    {'qc': 'QC2', 'containers': [{'id': 2, 'group': 'IF'}]},
# #                    {'qc': 'QC3', 'containers': [{'id': 3, 'group': 'IF'}]}]
# #     block_areas = [{'block': '1A', 'area': 2, 'plans': [{'group': 'IF', 'bay': '1A16', 'capacity': 21}],
# #                     'yc': {'name': 'YC1', 'location': 22},
# #                     'instructions': [{'type': None, 'status': 1, 'from': None, 'to': None, 'containerID': None}]}]
# # print(state.block_areas[0]['instructions'][0]['status'])



"""
测试取出status的代码
"""
# lists={21: {'unload': 120, 'onTruck': 240, 'arriveBlock': 300, 'offtruck': 300, 'finish': 480}, 97: {'unload': 120, 'onTruck': 240, 'arriveBlock': 300, 'offtruck': 480, 'finish': 660}}
# for id,list in lists.items():
#     print(list)
# """
# {'unload': 120, 'onTruck': 240, 'arriveBlock': 300, 'offtruck': 300, 'finish': 480}
# {'unload': 120, 'onTruck': 240, 'arriveBlock': 300, 'offtruck': 480, 'finish': 660}
# """
# test={'instructions': [{'type': 'U', 'status': '已配车', 'from': '', 'to': '1D30', 'containerID': 1}]}
# print(test['instructions'][0]['status'])


"""
测试取出当前箱区容量的代码
"""
# result={'block': '1D', 'area': 1, 'plans': [{'group': 'IF', 'bay': '1D02', 'capacity': 20}, {'group': 'IZ', 'bay': '1D22', 'capacity': 21}], 'yc': {'name': 'YC5', 'location': 34}, 'instructions': [{'type': 'U', 'status': '已配车', 'from': '', 'to': '1D22', 'containerID': 120}]}
# container_bay=result['instructions'][0]['to']
# plans = result['plans']
# for plan in plans:
#     if plan['bay']== container_bay:
#         print(plan['capacity'])
