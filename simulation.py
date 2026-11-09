from topology import connect, disconnect
from routing import find_shortest_path, count_path_hops


def create_network():
    return {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C", "E"],
        "E": ["D"],
        "F": [],
    }


def simulate(network, changes, start, end):
    """模拟拓扑事件并记录最短路径变化。"""
    shortest_path = find_shortest_path(
        network, start, end
    )  # 将初始路径记录到变量中，避免求跳数时再次运行 BFS
    history = [("initial", shortest_path, count_path_hops(shortest_path))]  # 初始化列表

    for change in changes:
        match change[0]:
            case "connect":
                connect(network, change[1], change[2])

            case "disconnect":
                disconnect(network, change[1], change[2])

            case _:
                raise ValueError("未知事件类型")

        shortest_path = find_shortest_path(network, start, end)
        history.append((change[0], shortest_path, count_path_hops(shortest_path)))
    return history
