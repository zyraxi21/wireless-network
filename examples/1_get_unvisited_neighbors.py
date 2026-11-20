network = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}

visited = {"A", "C"}

def get_unvisited_neighbors(network, node, visited):
    unvisited = []
    for neighbor in network[node]:
        if neighbor not in visited:
            unvisited.append(neighbor)
    return unvisited

print(get_unvisited_neighbors(network, "A", visited))
print(get_unvisited_neighbors(network, "D", visited))
