network = {
    "A": ["B"],
    "B": ["A"],
    "C": []
}

def connect(network, node1, node2):
    if node1 != node2:
        if node1 not in network[node2]:
            network[node2].append(node1)
        if node2 not in network[node1]:
            network[node1].append(node2)

connect(network, "A", "C")
connect(network, "A", "C")
connect(network, "B", "B")

print(network)