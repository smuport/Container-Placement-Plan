import random
import classification

cumulative_time = {'qc1': 0, 'qc2': 0, 'qc3': 0}

def getNextUnloadContainer(qc_name):
    # 在classification.work_queues中找到对应的岸桥
    qc_data = next((item for item in classification.work_queues if item['qc'] == qc_name), None)

    if qc_data is None:
        print(f"无效的岸桥名: {qc_name}")
        return None

    # 获取该岸桥的剩余集装箱列表
    containers = qc_data['containers']

    if not containers:
        print(f"该岸桥 {qc_name} 已经没有需要作业的集装箱了。")
        return None

    # 随机选择一个集装箱
    selected_container = random.choice(containers)

    # 生成作业时间：120 正负 3 的随机整数
    operation_time = random.randint(117, 123)

    # 更新累积作业时间
    cumulative_time[qc_name] += operation_time

    # 从列表中移除被选择的集装箱
    containers.remove(selected_container)

    # 输出结果
    output = f"{cumulative_time[qc_name]}, {selected_container}"
    print(output)

    return output

while True:
    qc_name = input("请输入岸桥名（qc1/qc2/qc3）或输入 'exit' 退出: ").strip().lower()
    if qc_name == 'exit':
        break
    result = getNextUnloadContainer(qc_name)
    if result is None:
        continue