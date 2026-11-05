from topology import connect, disconnect
from routing import find_shortest_path

network = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
    "F": [],
}

# 任务1：打印初始 A 到 E 的最短路径
print(find_shortest_path(network, "A", "E"))

# 任务2：断开 D—E，重新查找 A 到 E 的路径
disconnect(network, "D", "E")
print(find_shortest_path(network, "A", "E"))

# 任务3：建立 D—F，查找 A 到 F 的路径
connect(network, "D", "F")
print(find_shortest_path(network, "A", "F"))

# 任务4：断开 B—D，重新查找 A 到 F 的路径
disconnect(network, "B", "D")
print(find_shortest_path(network, "A", "F"))
