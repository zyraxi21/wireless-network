from topology import connect, disconnect
from routing import find_shortest_path, find_path_dfs
from simulation import simulate
import pytest


def create_network():
    """创建一个新的网络拓扑。

    Args:
        无参数。

    Returns:
        输出一个字典，包含数个网络节点和它们间的连接关系。

    Raises:
        无。

    Example:
        >>> network = create_network()
    """
    return {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C", "E"],
        "E": ["D"],
        "F": [],
    }


def test_connect_new_link():
    """测试新连接能否正常建立。

    Args:
        无参数。

    Returns:
        无输出。

    Raises:
        AssertionError: 未添加邻居节点时抛出。

    Example:
        >>> test_connect_new_link()
        AssertionError
    """
    network = create_network()

    connect(network, "A", "F")
    connect(network, "A", "F")

    assert network["A"].count("F") == 1
    assert network["F"].count("A") == 1


def test_duplicate_connection():
    """测试重复建立相同链路，不会产生重复邻居。

    Args:
        无参数。

    Returns:
        无输出。

    Raises:
        AssertionError: 未添加或重复添加邻居节点时抛出。

    Example:
        >>> test_duplicate_connection()
        AssertionError
    """
    network = create_network()

    connect(network, "A", "B")

    assert network["A"].count("B") == 1
    assert network["B"].count("A") == 1


def test_disconnect_twice():
    """测试连续断开两次相同链路，不会报错。

    Args:
        无参数。

    Returns:
        无输出。

    Raises:
        AssertionError: 断开已无连接的节点时抛出。

    Example:
        >>> test_disconnect_twice()
        AssertionError
    """
    network2 = create_network()
    disconnect(network2, "A", "B")
    disconnect(network2, "A", "B")
    assert network2["A"] == ["C"]
    assert network2["B"] == ["D"]


def test_shortest_path():
    """测试正常可达、不可达和起终点相同的情况。

    Args:
        无参数。

    Returns:
        无输出。

    Raises:
        AssertionError: BFS 函数找到的最短路径不正确时抛出。

    Example:
        >>> test_shortest_path()
        AssertionError
    """
    # 测试正常可达
    network = create_network()
    assert find_shortest_path(network, "A", "E") == ["A", "B", "D", "E"]

    # 测试不可达节点
    network4 = create_network()
    assert find_shortest_path(network4, "A", "F") is None

    # 测试起终点相同
    network3 = create_network()
    assert find_shortest_path(network3, "A", "A") == ["A"]


def test_simulation():
    """验证四次网络事件发生后的完整 history。

    Args:
        无参数。

    Returns:
        无输出。

    Raises:
        AssertionError: 四次网络事件发生后返回的 history 不正确时抛出。

    Example:
        >>> test_simulation()
        AssertionError
    """
    changes = [
        ("disconnect", "B", "D"),
        ("disconnect", "D", "E"),
        ("connect", "D", "F"),
        ("connect", "F", "E"),
    ]

    assert simulate(create_network(), changes, "A", "E") == [
        ("initial", ["A", "B", "D", "E"], 3),
        ("disconnect", ["A", "C", "D", "E"], 3),
        ("disconnect", None, None),
        ("connect", None, None),
        ("connect", ["A", "C", "D", "F", "E"], 4),
    ]

    assert simulate(create_network(), changes, "A", "A") == [
        ("initial", ["A"], 0),
        ("disconnect", ["A"], 0),
        ("disconnect", ["A"], 0),
        ("connect", ["A"], 0),
        ("connect", ["A"], 0),
    ]

    assert simulate(create_network(), changes, "E", "E") == [
        ("initial", ["E"], 0),
        ("disconnect", ["E"], 0),
        ("disconnect", ["E"], 0),
        ("connect", ["E"], 0),
        ("connect", ["E"], 0),
    ]

    assert simulate(create_network(), [], "A", "E") == [
        ("initial", ["A", "B", "D", "E"], 3)
    ]


def test_invalid_event():
    """验证遇到 "shutdown" 这样的未知事件时，会抛出 ValueError。

    Args:
        无参数。

    Returns:
        无输出。

    Raises:
        ValueError: 事件列表中有未知事件时抛出。

    Example:
        >>> test_invalid_event()
        ValueError
    """
    with pytest.raises(ValueError, match="未知事件类型"):
        simulate(create_network(), [("shutdown", "E", "F")], "A", "E")


# # 测试断开某条链路后，能否找到替代路径。
# network5 = create_network()
# assert find_shortest_path(network5, "A", "D") == ["A", "B", "D"]
# disconnect(network5, "A", "B")
# assert find_shortest_path(network5, "A", "D") == ["A", "C", "D"]

# # 测试建立 D—F 后能否找到 A 到 F 的最短路径
# network6 = create_network()
# connect(network6, "D", "F")

# assert network6["D"].count("F") == 1
# assert network6["F"].count("D") == 1
# assert find_shortest_path(network6, "A", "F") == ["A", "B", "D", "F"]

def test_path_dfs():
    """测试正常可达、不可达和起终点相同的情况。"""
    # 测试正常可达
    network = create_network()
    assert find_path_dfs(network, "A", "E") == ["A", "B", "D", "E"]

    # 测试不可达节点
    network4 = create_network()
    assert find_path_dfs(network4, "A", "F") is None

    # 测试起终点相同
    network3 = create_network()
    assert find_path_dfs(network3, "A", "A") == ["A"]

    # 测试不存在的节点
    with pytest.raises(ValueError, match="节点不存在"):
        find_path_dfs(network, "A", "G")