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


# def apply_changes(network, changes):
#     for change in changes:
#         match change[0]:
#             case "connect":
#                 connect(network, change[1], change[2])
#             case "disconnect":
#                 disconnect(network, change[1], change[2])
#             case _:
#                 pass
