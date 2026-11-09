def get_two_hop_neighbors(network, start):
    one_hop = []
    two_hops = []

    for neighbor1 in network[start]:
        one_hop.append(neighbor1)
    
    for node in one_hop:
        for neighbor2 in network[node]:
            if neighbor2 != start:
                if neighbor2 not in one_hop:
                    if neighbor2 not in two_hops:
                        two_hops.append(neighbor2)

    return one_hop + two_hops

network = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}

print(get_two_hop_neighbors(network, "A"))
