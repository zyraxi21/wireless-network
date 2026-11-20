def connect(network, node1, node2):
    if node1 != node2:
        if node1 not in network[node2]:
            network[node2].append(node1)
        if node2 not in network[node1]:
            network[node1].append(node2)

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

def find_shortest_path(network, start, end):
    if start == end:
        return [start]

    queue = [start]
    parent = {start: None}
    
    while queue:
        current = queue.pop(0)

        for neighbor in network[current]:
            if neighbor not in parent:
                queue.append(neighbor)
                parent[neighbor] = current

                if neighbor == end:
                    path = [end]
                    stopover = end
                    while stopover != start:
                        path.append(parent[stopover])
                        stopover = parent[stopover]
                    path.reverse()
                    return path

    return None

network = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
    "F": []
}

assert find_shortest_path(network, "A", "E") == ['A', 'B', 'D', 'E']
assert find_shortest_path(network, "D", "A") == ['D', 'B', 'A']
assert find_shortest_path(network, "A", "F") is None
assert find_shortest_path(network, "A", "A") == ['A']
assert find_shortest_path(network, "F", "F") == ['F']
assert find_shortest_path(network, "A", "B") == ['A', 'B']

connect(network, "D", "F")
disconnect(network, "D", "E")

assert find_shortest_path(network, "A", "E") is None
assert find_shortest_path(network, "D", "A") == ['D', 'B', 'A']
assert find_shortest_path(network, "A", "F") == ['A', 'B', 'D', 'F']
assert find_shortest_path(network, "A", "A") == ['A']
assert find_shortest_path(network, "F", "F") == ['F']
assert find_shortest_path(network, "A", "B") == ['A', 'B']

disconnect(network, "B", "D")

assert find_shortest_path(network, "A", "D") == ['A', 'C', 'D']