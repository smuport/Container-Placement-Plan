from randomContainer import getNextUnloadContainer
# from ubload_old import allocate
from ubload import allocate
from classification import state


class Event:
    def __init__(self, name, data, callback):
        self.name = name
        self.data = data
        self.callback = callback


task_dict = {
    'Aplan': {'task_list': [], 'arrive_time': [], 'finish_time': [], 'wait_times': []},
    'Bplan': {'task_list': [], 'arrive_time': [], 'finish_time': [], 'wait_times': []},
    'C1plan': {'task_list': [], 'arrive_time': [], 'finish_time': [], 'wait_times': []},
    'C2plan': {'task_list': [], 'arrive_time': [], 'finish_time': [], 'wait_times': []},
    'Dplan': {'task_list': [], 'arrive_time': [], 'finish_time': [], 'wait_times': []}
}


class EventScheduler:
    def __init__(self):
        # 初始化事件队列
        self.eventQueue = []
        #设置一个字典储存每个箱子的卸船等待事件
        self.container_timelist={}

    def add(self, time: int, event: Event):
        self.eventQueue.append((time, event))
        self.eventQueue.sort(key=lambda x: x[0], reverse=False)  #按时间排序

    def step(self):
        # 取出队首事件
        if not self.eventQueue:
            return
        time, event = self.eventQueue.pop(0)
        # 调用事件的回调函数
        event.callback(event)

    def run(self):
        time = 0
        for data in [{'qc': 'qc1', 'container': {'id': None}}, {'qc': 'qc2', 'container': {'id': None}},
                     {'qc': 'qc3', 'container': {'id': None}}]:
            time = time + 1
            data['time'] = time
            FirstUnloadEvent = Event('FirstUnloadEvent', data, unloadCallback)
            self.add(time, FirstUnloadEvent)
            # print(self.eventQueue)
        while self.eventQueue:
            self.step()

"""
这里存在问题 每个箱子的等待时间的和不应该是总等待时间 
"""
def sumWaitTime(task_list):
    totalWaitTime = 0
    for plan_name in task_list:
        planlWaitTime = sum(task_dict[plan_name]['wait_times'])
        print(f'当前{plan_name}的等待时间是{planlWaitTime}秒')
        totalWaitTime += planlWaitTime
    return totalWaitTime
def caculateWaitTime(task_dict, plan_name):
    """
    从plan取出来的字典中取出每一个场桥执行的任务 进行判断 如果箱子index=i+1的到达箱区时间<index=i的结束时间 确定会产生等待时间
    如果产生了等待 那么index=i的finsihtime-index=i+1的arrivetime就是等待时间
    按理来说 每个箱区的第一个任务都不会产生等待时间
    那么如何判断是否存在等待时间呢 也即上述提到的差值 如果小于0那么就没有等待时间  也即等待时间加0
    这个函数的逻辑应该是分别计算每个箱区的等待时间 那么一开始就应该是取出不同的计划和对应的到达时间
    """
    global wait_time, ft
    plan_info = task_dict[plan_name]
    arrive_time = plan_info['arrive_time']
    finish_time = []
    wait_times = []
    for i in range(len(arrive_time)):
        if i == 0:
            wait_time = 0
            ft = arrive_time[i] + 180
        elif i != 0:
            if finish_time[i - 1] > arrive_time[i]:
                wait_time = finish_time[i - 1] - arrive_time[i]
                ft = arrive_time[i] + 180 + wait_time
            else:
                wait_time = 0
                ft = arrive_time[i] + 180
        finish_time.append(ft)
        wait_times.append(wait_time)
    plan_info['wait_times'] = wait_times
    plan_info['finish_time'] = finish_time
    return task_dict

def unloadCallback(event: Event):
    global scheduler
    qc = event.data['qc']
    time = event.data['time']

    all_capacity = 0

    # capacityIF=event.data['container']['plans']
    name=event.name
    # id = event.data['container']['id']
    # print(f'当前的集装箱{id}，执行的操作是{name}，当前的时间是{time}s')
    # """
    # 记录卸船完成事件到container_timelist中
    # """
    # if id not in scheduler.container_timelist:
    #     scheduler.container_timelist[id] = {
    #         'unload_time': time,
    #         'unload_bay': 'N/A',
    #         'unload_capacity': 0,
    #         'onTruck_time': 'N/A',
    #         'arriveBlock_time': 'N/A',
    #         'offtruck_time': 'N/A',
    #         'finish_time': 'N/A'
    #     }
    # else:
    #     scheduler.container_timelist[id]['unload_time'] = time

    nextContainer = getNextUnloadContainer(qc)
    # step1: 随机选择下一个卸船，并排入事件轴
    if nextContainer is not None:
            unload_time = nextContainer[0]
            container = nextContainer[1]
            id = container['id']
            print(f'当前的集装箱{id}，执行的操作是{name}，当前的时间是{time}s')
            """
            记录卸船完成事件到container_timelist中
            """
            if id not in scheduler.container_timelist:
                scheduler.container_timelist[id] = {
                    'unload_time': time,
                    'unload_bay': 'N/A',
                    'unload_capacity': 0,
                    'onTruck_time': 'N/A',
                    'arriveBlock_time': 'N/A',
                    'offtruck_time': 'N/A',
                    'finish_time': 'N/A'
                }
            else:
                scheduler.container_timelist[id]['unload_time'] = time
        # 创建 unload Event
            nextUnloadEvent = Event("unload", {'qc': qc, 'container': container,'time':unload_time}, unloadCallback)
            scheduler.add(unload_time, nextUnloadEvent)
            # step2：选位决策,生成作业指令 接收到箱子的堆场贝位信息 return {group: "IZ", bay: "1A20", capacity: 10}
            for block_area in state.block_areas:
                for plan in block_area['plans']:
                    all_capacity = plan['capacity']+all_capacity
            # print(container)
            print(all_capacity)
            if all_capacity != 0:
                my_choose,result = allocate(state, container)
                result['instructions'][0]['from'] = qc
                result['instructions'][0]['containerID'] = container['id']
                status='已配车'
                updateBlock_areas(result,status)
                """
                ??????
                3.状态函数的使用也要基于instruction添加完后再进
                """
                # print(result)
                #这里是更新箱区容量
                for area in state.block_areas:
                    if area['block'] == result['block'] and area['area'] == result['area']:
                        area['instructions'][0]['to'] = my_choose['bay']
                        for plan in area['plans']:
                            if plan['group'] == my_choose['group']:
                                plan['capacity'] -=1

                """
                把箱子的去向和当前箱区容量一起存在scheduler.container_timelist中去
                """
                container_bay=result['instructions'][0]['to']
                scheduler.container_timelist[id]['unload_bay'] = container_bay
                print(container_bay)
                if container_bay == 'N/A':
                    print('my_choose bay:',my_choose['bay'])
                plans = result['plans']
                for plan in plans:
                    if plan['bay'] == container_bay:
                        scheduler.container_timelist[id]['unload_capacity'] = plan['capacity']
                # 创建当前箱子的集卡运输事件
                ontruck_time = unload_time + 120
                nextOnTruckEvent = Event("onTruck", {'qc': qc, 'container': container,'time':ontruck_time,'result':result}, onTruckCallback)
                scheduler.add(ontruck_time, nextOnTruckEvent)

                #到达箱区事件
                arrive_time=ontruck_time+60
                nextArriveEvent= Event("arriveBlock", {'qc': qc, 'container': container,'time':arrive_time,'result':result}, arriveBlockCallback)
                scheduler.add(arrive_time, nextArriveEvent)

                # 释车事件,有点问题offtruck_time计算不准确
                updated = updateTask_dict(result, unload_time)
                task_dict = updated[0]
                plan = updated[1]
                id = container['id']
                index = task_dict[plan]['task_list'].index(id)
                offtruck_time = task_dict[plan]['finish_time'][index] - 180
                nextOfftruckEvent = Event("offtruck", {'qc': qc, 'container': container,'time':offtruck_time,'result':result}, offtruckCallback)
                scheduler.add(offtruck_time, nextOfftruckEvent)

                # 结束任务事件
                """
                只要当前任务开始被执行 我们就把他的完成时间输出进去存起来 
                卸船2 运输1 作业3 等待？？
                """
                finish_time = task_dict[plan]['finish_time'][index]
                nextFinishEvent = Event("finish", {'qc': qc, 'container': container,'time':finish_time,'result':result}, finishCallback)
                scheduler.add(finish_time, nextFinishEvent)
    else:
        current_time = time
        print(f'桥吊{qc}作业已完成，完成的时间是{current_time}')
        # scheduler.step()
def onTruckCallback(event):
    global scheduler
    id=event.data['container']['id']
    name=event.name
    time=event.data['time']
    status='已压车'
    updateBlock_areas(event.data['result'], status)
    print(f'当前的集装箱{id}，执行的操作是{name}，当前的时间是{time}s')
    scheduler.container_timelist[id]['onTruck_time'] = time

def arriveBlockCallback(event):
    global scheduler
    id = event.data['container']['id']
    name = event.name
    time = event.data['time']
    status='已到箱区'
    updateBlock_areas(event.data['result'], status)
    print(f'当前的集装箱{id}，执行的操作是{name}，当前的时间是{time}s')
    scheduler.container_timelist[id]['arriveBlock_time'] = time

def offtruckCallback(event):
    global scheduler
    id = event.data['container']['id']
    name = event.name
    time = event.data['time']
    status = '已释车'
    updateBlock_areas(event.data['result'], status)
    print(f'当前的集装箱{id}，执行的操作是{name}，当前的时间是{time}s')
    scheduler.container_timelist[id]['offtruck_time'] = time


def finishCallback(event):
    global scheduler
    id = event.data['container']['id']
    name = event.name
    time = event.data['time']
    status = '已完成'
    updateBlock_areas( event.data['result'], status)
    print(f'当前的集装箱{id}，执行的操作是{name}，当前的时间是{time}s')
    scheduler.container_timelist[id]['finish_time'] = time

# my_choose={'group': 'OZ', 'bay': '1C18', 'capacity': 6}
# result = {'block': '1D', 'area': 2,
#           'plans': [{'group': 'IF', 'bay': '1D30', 'capacity': 16}],
#           'yc': {'name': 'YC5', 'location': 34},
#           'instructions': [{'type': 'U', 'status': '已配车', 'from': 'qc1', 'to': '1D30', 'containerID': 53}]}


def updateTask_dict(result, unload_time):
    global plan
    container_id = result['instructions'][0]['containerID']
    result_block = result['block']
    result_area = result['area']

    if result_block == '1A':
        plan = 'Aplan'
    elif result_block == '1B':
        plan = 'Bplan'
    elif result_block == '1C':
        if result_area == 2:
            plan = 'C2plan'
        else:
            plan = 'C1plan'
    elif result_block == '1D':
        plan = 'Dplan'

    task_dict[plan]['task_list'].append(container_id)
    task_dict[plan]['arrive_time'].append(unload_time + 180)

    caculateWaitTime(task_dict, plan)
    return task_dict, plan

"""
更新全局变量中的blockarea的方法 包括加入每一个新的instructions和更新当前的instructions的status  
"""
def updateBlock_areas(result,status):
    # for result in results:
    blockareas = state.block_areas
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
    state.block_areas = blockareas
    return blockareas


scheduler = EventScheduler()
scheduler.run()

# print(f"最后的任务列表是：{task_dict}")

for container_id,time_list in scheduler.container_timelist.items():
    if container_id is not None:
        print(f'集装箱{container_id}，去往{time_list["unload_bay"]}，当前箱区容量{time_list["unload_capacity"]}：')
        print(f'卸船时间：{time_list["unload_time"]}s')
        print(f'装车时间：{time_list["onTruck_time"]}s')
        print(f'到达箱区时间：{time_list["arriveBlock_time"]}s')
        print(f'释车时间：{time_list["offtruck_time"]}s')
        print(f'卸船时间：{time_list["finish_time"]}s')
print(f"总共等待时间是：{sumWaitTime(task_dict.keys())}")

print(state.block_areas)