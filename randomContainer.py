from classification import state  # 从 classification.py 文件中导入 State 类
import random
from typing import Dict, Any, Tuple, List


def getAllUnloadContainers(state: state) -> list[tuple[float, Any]]:
    """
    为所有集装箱生成随机卸载时间。
    :param state: 全局 State 对象
    :return: 包含所有集装箱及其卸载时间的列表，格式为 [(unload_time, container), ...]
    """
    all_containers = []

    # 遍历所有岸桥的集装箱
    for work_queue in state.work_queues:
        for container in work_queue["containers"]:
            unload_time = random.normalvariate(120, 3)
            all_containers.append((round(unload_time, 2), container))  # 保留两位小数

    return all_containers


# 示例调用
if __name__ == "__main__":
    state = state()  # 创建 State 对象
    try:
        all_containers = getAllUnloadContainers(state)
        for unload_time, container in all_containers:
            print(f"卸载时间: {unload_time} 秒, 集装箱: {container}")
    except ValueError as e:
        print(e)