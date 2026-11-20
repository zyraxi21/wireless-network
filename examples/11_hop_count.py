def get_hop_counts(network, start):
    queue = [start]
    visited = {start}
    distance = {start: 0}
    while queue:
        current = queue.pop(0)
        for neighbor in network[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                distance[neighbor] = distance[current] + 1
                visited.add(neighbor)
    return distance


network = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
    "F": []
}

print(get_hop_counts(network, "A"))
print(get_hop_counts(network, "D"))
print(get_hop_counts(network, "F"))
