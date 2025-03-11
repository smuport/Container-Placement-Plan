import random
import classification

cumulative_time = {'qc1': 0, 'qc2': 0, 'qc3': 0}


def getNextUnloadContainer(qc_name):
    qc_data = next((item for item in classification.work_queues if item['qc'] == qc_name), None)

    if qc_data is None:
        print(f"无效的岸桥名: {qc_name}")
        return None

    containers = qc_data['containers']

    if not containers:
        print(f"该岸桥 {qc_name} 已经没有需要作业的集装箱了。")
        return None
    # 按顺序排列发箱

    # selected_container = containers.pop(0)
    # operation_time = 120
    # cumulative_time[qc_name] += operation_time
    # 随机发箱
    selected_container = random.choice(containers)
    operation_time = random.randint(117, 123)
    containers.remove(selected_container)
    cumulative_time[qc_name] += operation_time
    # output = f"{cumulative_time[qc_name]}, {selected_container}"

    return cumulative_time[qc_name], selected_container

# while True:
#     qc_name = input("请输入岸桥名（qc1/qc2/qc3）或输入 'exit' 退出: ").strip().lower()
#     if qc_name == 'exit':
#         break
#     result = getNextUnloadContainer(qc_name)
#     if result is None:
#         continue
