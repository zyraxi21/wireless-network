from topology import connect, disconnect
from routing import find_shortest_path


def create_network():
    return {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C", "E"],
        "E": ["D"],
        "F": [],
    }


# 测试新连接能否正常建立
network = create_network()

connect(network, "A", "F")
connect(network, "A", "F")

assert network["A"].count("F") == 1
assert network["F"].count("A") == 1


# 测试建立已经存在的链路，不会重复添加。
network1 = create_network()
connect(network1, "A", "B")

assert network1["A"].count("B") == 1
assert network1["B"].count("A") == 1

# 测试连续两次断开同一条链路，不会报错。
network2 = create_network()
disconnect(network2, "A", "B")
disconnect(network2, "A", "B")
assert network2["A"] == ["C"]
assert network2["B"] == ["D"]

# 测试起终点相同。
network3 = create_network()
assert find_shortest_path(network3, "A", "A") == ["A"]

# 测试不可达节点。
network4 = create_network()
assert find_shortest_path(network4, "A", "F") is None

# 测试断开某条链路后，能否找到替代路径。
network5 = create_network()
assert find_shortest_path(network5, "A", "D") == ["A", "B", "D"]
disconnect(network5, "A", "B")
assert find_shortest_path(network5, "A", "D") == ["A", "C", "D"]

# 测试建立 D—F 后能否找到 A 到 F 的最短路径
network6 = create_network()
connect(network6, "D", "F")

assert network6["D"].count("F") == 1
assert network6["F"].count("D") == 1
assert find_shortest_path(network6, "A", "F") == ["A", "B", "D", "F"]
