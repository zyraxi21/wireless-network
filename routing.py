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


def count_path_hops(path):
    if path is None:
        return None
    return len(path) - 1


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

def find_path_dfs(network, start, end):
    if start not in network or end not in network:
        raise ValueError("节点不存在")

    if start == end:
        return [start]
    
    path = [start]
    visited = {start}

    while path and path[-1] != end:
        exist = False
        for neighbor in network[path[-1]]:
            if neighbor not in visited:
                path.append(neighbor)
                visited.add(neighbor)
                exist = True
                break
        
        if not exist:
            path.pop()
        
    if not path:
        return None
    
    return path
