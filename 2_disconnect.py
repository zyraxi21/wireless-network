network = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}

def disconnect(network, node1, node2):
    if node2 in network[node1]:
        if node1 in network[node2]:
            network[node1].remove(node2)
            network[node2].remove(node1)
        else:
            network[node1].remove(node2)
    else:
        if node1 in network[node2]:
            network[node2].remove(node1)

disconnect(network, "B", "D")

print(network["B"])
print(network["D"])
