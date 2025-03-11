# blockareas={"blockAreas": [
#         {
#             "block": "1A",
#             "area": 1,
#             "plans": [
#                 {
#                     "group": "IF",
#                     "bay": "1A02",
#                     "capacity": 21
#                 }
#             ],
#             "yc": {
#                 "name": "YC1",
#                 "location": 34
#             },
#             "instructions": [
#                 {
#                     "type": "U",
#                     "status": '',
#                     "from": '',
#                     "to": '',
#                     "containerID": ''
#                 }
#             ]
#         },
#         {
#             "block": "1A",
#             "area": 2,
#             "plans": [
#                 {
#                     "group": "IF",
#                     "bay": "1A30",
#                     "capacity": 21
#                 }
#             ],
#             "yc": {
#                 "name": "YC1",
#                 "location": 34
#             },
#             "instructions": [
#                 {
#                     "type": "U",
#                     "status": '',
#                     "from": '',
#                     "to": '',
#                     "containerID": ''
#                 }
#             ]
#         },
#         {
#             "block": "1B",
#             "area": 1,
#             "plans": [
#                 {
#                     "group": "IF",
#                     "bay": "1B02",
#                     "capacity": 21
#                 },
#                 {
#                     "group": "IZ",
#                     "bay": "1B22",
#                     "capacity": 21
#                 }
#             ],
#             "yc": {
#                 "name": "YC2",
#                 "location": 34
#             },
#             "instructions": [
#                 {
#                     "type": "U",
#                     "status": '',
#                     "from": '',
#                     "to": '',
#                     "containerID": ''
#                 }
#             ]
#         },
#         {
#             "block": "1B",
#             "area": 2,
#             "plans": [
#                 {
#                     "group": "IF",
#                     "bay": "1B30",
#                     "capacity": 21
#                 }
#             ],
#             "yc": {
#                 "name": "YC2",
#                 "location": 34
#             },
#             "instructions": [
#                 {
#                     "type": "U",
#                     "status": '',
#                     "from": '',
#                     "to": '',
#                     "containerID": ''
#                 }
#             ]
#         },
#         {
#             "block": "1C",
#             "area": 1,
#             "plans": [
#                 {
#                     "group": "IF",
#                     "bay": "1C02",
#                     "capacity": 21
#                 },
#                 {
#                     "group": "OZ",
#                     "bay": "1C18",
#                     "capacity": 21
#                 }
#             ],
#             "yc": {
#                 "name": "YC3",
#                 "location": 22
#             },
#             "instructions": [
#                 {
#                     "type": "U",
#                     "status": '',
#                     "from": '',
#                     "to": '',
#                     "containerID": ''
#                 }
#             ]
#         },
#         {
#             "block": "1C",
#             "area": 2,
#             "plans": [
#                 {
#                     "group": "IF",
#                     "bay": "1C30",
#                     "capacity": 21
#                 }
#             ],
#             "yc": {
#                 "name": "YC4",
#                 "location": 34
#             },
#             "instructions": [
#                 {
#                     "type": "U",
#                     "status": '',
#                     "from": '',
#                     "to": '',
#                     "containerID": ''
#                 }
#             ]
#         },
#         {
#             "block": "1D",
#             "area": 1,
#             "plans": [
#                 {
#                     "group": "IF",
#                     "bay": "1D02",
#                     "capacity": 21
#                 },
#                 {
#                     "group": "IZ",
#                     "bay": "1D22",
#                     "capacity": 21
#                 }
#             ],
#             "yc": {
#                 "name": "YC5",
#                 "location": 34
#             },
#             "instructions": [
#                 {
#                     "type": "U",
#                     "status": '',
#                     "from": '',
#                     "to": '',
#                     "containerID": ''
#                 }
#             ]
#         },
#         {
#             "block": "1D",
#             "area": 2,
#             "plans": [
#                 {
#                     "group": "IF",
#                     "bay": "1D30",
#                     "capacity": 21
#                 }
#             ],
#             "yc": {
#                 "name": "YC5",
#                 "location": 34
#             },
#             "instructions": [
#                 {
#                     "type": "U",
#                     "status": '',
#                     "from": '',
#                     "to": '',
#                     "containerID": ''
#                 }
#             ]
#         }
#     ]}
# # results=[{'block': '1D', 'area': 2, 'plans': [{'group': 'IF', 'bay': '1D30', 'capacity': 16}], 'yc': {'name': 'YC5', 'location': 34}, 'instructions': [{'type': 'U', 'status': '已配车', 'from':'', 'to': '1D30', 'containerID': 45}]},
# #          {'block': '1D', 'area': 1, 'plans': [{'group': 'IF', 'bay': '1D02', 'capacity': 0}, {'group': 'IZ', 'bay': '1D22', 'capacity': 3}], 'yc': {'name': 'YC5', 'location': 34}, 'instructions': [{'type': 'U', 'status': '已配车', 'from': '', 'to': '1D22', 'containerID': 81}]},
# #          {'block': '1D', 'area': 1, 'plans': [{'group': 'IF', 'bay': '1D02', 'capacity': 0}, {'group': 'IZ', 'bay': '1D22', 'capacity': 2}], 'yc': {'name': 'YC5', 'location': 34}, 'instructions': [{'type': 'U', 'status': '已配车', 'from': '', 'to': '1D22', 'containerID': 76}]}]
# result={'block': '1D', 'area': 1, 'plans': [{'group': 'IF', 'bay': '1D02', 'capacity': 0}, {'group': 'IZ', 'bay': '1D22', 'capacity': 3}], 'yc': {'name': 'YC5', 'location': 34}, 'instructions': [{'type': 'U', 'status': '已配车', 'from': '', 'to': '1D22', 'containerID': 81}]}
# """
# 这个方法应该还是要分开 因为在每个callback函数调用的时候都会传入result 可能会造成重复apppend的情况 或者写一个if else
# """
# def updateBlock_areas(blockareas,result,status):
#     # for result in results:
#         blockAreas = blockareas['blockAreas']
#         for i in range(len(blockAreas)):
#             block = blockAreas[i]['block']
#             area = blockAreas[i]['area']
#             instructions = blockAreas[i]['instructions']
#             if block == result['block'] and area == result['area']:
#                 """
#                 if id不存在 插入 else执行更改status的逻辑
#                 """
#                 for instruction in instructions:
#                     if instruction['containerID'] == result['instructions'][0]['containerID']:
#                         instruction['status'] = status
#                         break
#                 else:
#                     if instructions[0]['containerID'] == '':
#                         instructions.pop(0)
#                     instructions.append((result['instructions'][0]))
#         return blockareas
#
#
#
# status=result['instructions'][0]['status']
# updateBlock_areas(blockareas,result,status)
# print(blockareas)
# status='已到箱区'
# updateBlock_areas(blockareas,result,status)
# print(blockareas)
# status='已完成'
# updateBlock_areas(blockareas,result,status)
# print(blockareas)
# # change_status(blockareas,result,status)
# # print(blockareas)
#
#
#
#
# #
# import state
# print(state.block_areas)
"""
测试更新箱区全局状态的代码
"""
blockareas=[{'block': '1A',
             'area': 1,
             'plans': [{'group': 'IF', 'bay': '1A02', 'capacity': 21}],
             'yc': {'name': 'YC1', 'location': 34},
             'instructions': [{'type': 'U', 'status': '', 'from': '', 'to': '', 'containerID': ''}]},
            {'block': '1A',
             'area': 2,
             'plans': [{'group': 'IF', 'bay': '1A30', 'capacity': 21}],
             'yc': {'name': 'YC1', 'location': 34},
             'instructions': [{'type': 'U', 'status': '', 'from': '', 'to': '', 'containerID': ''}]},
            {'block': '1B',
             'area': 1,
             'plans': [{'group': 'IF', 'bay': '1B02', 'capacity': 21}, {'group': 'IZ', 'bay': '1B22', 'capacity': 21}],
             'yc': {'name': 'YC2', 'location': 34},
             'instructions': [{'type': 'U', 'status': '', 'from': '', 'to': '', 'containerID': ''}]},
            {'block': '1B', 'area': 2,
             'plans': [{'group': 'IF', 'bay': '1B30', 'capacity': 21}],
             'yc': {'name': 'YC2', 'location': 34},
             'instructions': [{'type': 'U', 'status': '', 'from': '', 'to': '', 'containerID': ''}]},
            {'block': '1C',
             'area': 1,
             'plans': [{'group': 'IF', 'bay': '1C02', 'capacity': 21}, {'group': 'OZ', 'bay': '1C18', 'capacity': 21}],
             'yc': {'name': 'YC3', 'location': 22},
             'instructions': [{'type': 'U', 'status': '', 'from': '', 'to': '', 'containerID': ''}]},
            {'block': '1C',
             'area': 2,
             'plans': [{'group': 'IF', 'bay': '1C30', 'capacity': 21}],
             'yc': {'name': 'YC4', 'location': 34},
             'instructions': [{'type': 'U', 'status': '', 'from': '', 'to': '', 'containerID': ''}]},
            {'block': '1D',
             'area': 1,
             'plans': [{'group': 'IF', 'bay': '1D02', 'capacity': 21}, {'group': 'IZ', 'bay': '1D22', 'capacity': 21}],
             'yc': {'name': 'YC5', 'location': 34},
             'instructions': [{'type': 'U', 'status': '', 'from': '', 'to': '', 'containerID': ''}]},
            {'block': '1D',
             'area': 2,
             'plans': [{'group': 'IF', 'bay': '1D30', 'capacity': 21}],
             'yc': {'name': 'YC5', 'location': 34},
             'instructions': [{'type': 'U', 'status': '', 'from': '', 'to': '', 'containerID': ''}]}
            ]
# results=[{'block': '1D', 'area': 2, 'plans': [{'group': 'IF', 'bay': '1D30', 'capacity': 16}], 'yc': {'name': 'YC5', 'location': 34}, 'instructions': [{'type': 'U', 'status': '已配车', 'from':'', 'to': '1D30', 'containerID': 45}]},
#          {'block': '1D', 'area': 1, 'plans': [{'group': 'IF', 'bay': '1D02', 'capacity': 0}, {'group': 'IZ', 'bay': '1D22', 'capacity': 3}], 'yc': {'name': 'YC5', 'location': 34}, 'instructions':
#          {'block': '1D', 'area': 1, 'plans': [{'group': 'IF', 'bay': '1D02', 'capacity': 0}, {'group': 'IZ', 'bay': '1D22', 'capacity': 2}], 'yc': {'name': 'YC5', 'location': 34}, 'instructions': [{'type': 'U', 'status': '已配车', 'from': '', 'to': '1D22', 'containerID': 76}]}]
result={'block': '1D', 'area': 2, 'plans': [{'group': 'IF', 'bay': '1D02', 'capacity': 0}, {'group': 'IZ', 'bay': '1D22', 'capacity': 3}], 'yc': {'name': 'YC5', 'location': 34}, 'instructions': [{'type': 'U', 'status': '已配车', 'from': '', 'to': '1D22', 'containerID': 81}]}
def updateBlock_areas(blockareas,results,status):
    # for result in results:
        for i in range(len(blockareas)):
            block = blockareas[i]['block']
            area = blockareas[i]['area']
            instructions = blockareas[i]['instructions']
            if block == result['block'] and area == result['area']:
                """
                if id不存在 插入 else执行更改status的逻辑
                """
                for instruction in instructions:
                    if instruction['containerID'] == result['instructions'][0]['containerID']:
                        instruction['status'] = status
                        break
                else:
                    if instructions[0]['containerID'] == '':
                        instructions.pop(0)
                    instructions.append((result['instructions'][0]))
        return blockareas
status=result['instructions'][0]['status']
updateBlock_areas(blockareas,result,status)
print(blockareas)
status='已到箱区'
updateBlock_areas(blockareas,result,status)
print(blockareas)
status='已完成'
updateBlock_areas(blockareas,result,status)
print(blockareas)
# change_status(blockareas,result,status)
# print(blockareas)