import json

from state import work_queues, block_areas

with open('output.json', 'r') as file:
    data = json.load(file)


class state:
    work_queues = data.get('workQueues', [])
    block_areas = data.get('blockAreas', [])


class containers:
    containers = []
    for work_queue in work_queues:
        containers.extend(work_queue.get('containers', []))


class WorkQueue:
    WorkQueue = []
    for item in work_queues:
        WorkQueue.append(item['qc'])


class plans:
    plans = []


class information:
    yc_information = []


class instructions:
    instructions = []
#
#
# for block_area in block_areas:
#     plans = []
#
#     plans.extend(block_area.get('plans', []))
#
#     yc = block_area.get('yc', {})
#     yc_information = []
#     if yc:
#         yc_information.append(yc)
#
#     instructions = []
#     instructions.extend(block_area.get('instructions', []))

# print("WorkQueues:", work_queues)
# print("Containers:", containers)
# print("BlockAreas:", block_areas)
# print("Plans:", plans)
# print("yc:", information.yc_information)
# print("Instructions:", instructions)
# print("qc:", qcs)
