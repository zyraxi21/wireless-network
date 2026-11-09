def get_reachable_nodes(network, start):
    queue = [start]
    visited = {start}
    result = []
    while queue:
        current = queue.pop(0)
        for node in network[current]:
            if node not in visited:
                queue.append(node)
                result.append(node)
                visited.add(node)
    return result


network = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
    "F": []
}

print(get_reachable_nodes(network, "A"))
print(get_reachable_nodes(network, "D"))
print(get_reachable_nodes(network, "F"))
