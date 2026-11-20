"""练习 12：把 API 返回的链路表转成邻接表。"""

import json


def topology_from_payload(payload):
    """从 payload 里取出节点和链路，返回双向邻接表。

    payload 的形状是这样的：

        {
            "network": {
                "nodes": ["A", "B", "C"],
                "links": [
                    {"source": "A", "target": "B", "latency_ms": 12},
                    {"source": "B", "target": "C", "latency_ms": 8},
                ]
            }
        }

    要求：
    1. 邻接表的节点以 "nodes" 为准，即使没有邻居也要出现，值为空列表；
    2. "links" 里每条链路是双向的，source 和 target 两边都要记；
    3. 链路指向的节点如果不在 "nodes" 里，说明数据是脏的，跳过这条；
    4. latency_ms 这一课先不用，阶段 2 学 Dijkstra 时再捡起来。

    提示：你写 connect() 的时候处理过"一条边要记两个方向"，这里是同一个问题。
    """
    # 你来实现
    network = {}
    for node in payload["network"]["nodes"]:
        network[node] = []
    links = payload["network"]["links"]
    for link in links:
        source = link["source"]
        target = link["target"]
        if source in network and target in network and source != target:
            if target not in network[source]:
                network[source].append(target)
            if source not in network[target]:
                network[target].append(source)
    return network


if __name__ == "__main__":
    text = """{
        "network": {
            "nodes": ["A", "B", "C", "D"],
            "links": [
                {"source": "A", "target": "B", "latency_ms": 12},
                {"source": "A", "target": "C", "latency_ms": 30},
                {"source": "B", "target": "D", "latency_ms": 8}
            ]
        }
    }"""

    payload = json.loads(text)

    # 第一组：正常数据
    # payload = {
    #     "network": {
    #         "nodes": ["A", "B", "C", "D"],
    #         "links": [
    #             {"source": "A", "target": "B", "latency_ms": 12},
    #             {"source": "A", "target": "C", "latency_ms": 30},
    #             {"source": "B", "target": "D", "latency_ms": 8},
    #         ],
    #     }
    # }
    print(topology_from_payload(payload))

    # 第二组：有节点，但没有链路
    empty = {"network": {"nodes": ["X", "Y"], "links": []}}
    print(topology_from_payload(empty))

    # 第三组：链路里混进了不存在的节点
    dirty = {
        "network": {
            "nodes": ["A", "B"],
            "links": [
                {"source": "A", "target": "B", "latency_ms": 5},
                {"source": "A", "target": "Z", "latency_ms": 5},
            ],
        }
    }
    print(topology_from_payload(dirty))
