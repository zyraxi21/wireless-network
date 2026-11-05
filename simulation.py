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


changes = [
    ("disconnect", "B", "D"),
    ("disconnect", "D", "E"),
    ("connect", "D", "F"),
    ("connect", "F", "E"),
]

assert simulate(create_network(), changes, "A", "E") == [
    ("initial", ["A", "B", "D", "E"], 3),
    ("disconnect", ["A", "C", "D", "E"], 3),
    ("disconnect", None, None),
    ("connect", None, None),
    ("connect", ["A", "C", "D", "F", "E"], 4),
]

assert simulate(create_network(), changes, "A", "A") == [
    ("initial", ["A"], 0),
    ("disconnect", ["A"], 0),
    ("disconnect", ["A"], 0),
    ("connect", ["A"], 0),
    ("connect", ["A"], 0),
]

assert simulate(create_network(), changes, "E", "E") == [
    ("initial", ["E"], 0),
    ("disconnect", ["E"], 0),
    ("disconnect", ["E"], 0),
    ("connect", ["E"], 0),
    ("connect", ["E"], 0),
]

assert simulate(create_network(), [], "A", "E") == [
    ("initial", ["A", "B", "D", "E"], 3)
]

try:
    simulate(create_network(), [("shutdown", "E", "F")], "A", "E")
except ValueError:
    print("测试通过：正确抛出 ValueError")
else:
    raise AssertionError("测试失败：没有抛出 ValueError")
