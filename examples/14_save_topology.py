"""练习 14：把拓扑存成 JSON 文件，再读回来。"""

import json
from pathlib import Path


def save_topology(network, path):
    """把邻接表 network 写成 JSON 文件，保存到 path。只写文件，不返回数据。

    要求：
    1. 用 UTF-8 编码写（Windows 默认 GBK，不显式写会乱码）；
    2. 中文原样保存，不要变成 \\uXXXX；
    3. 缩进 2 个空格，方便人看。
    """
    text = json.dumps(network, ensure_ascii=False, indent=2)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def load_topology(path):
    """从 path 指向的 JSON 文件读回邻接表，返回 dict。"""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    network = {"节点A": ["节点B"], "节点B": ["节点A"]}
    path = Path(__file__).with_name("_topology_demo.json")

    save_topology(network, path)
    loaded = load_topology(path)

    assert loaded == network
    print("读回来和原来一样吗：", loaded == network)
    print("文件内容：")
    print(path.read_text(encoding="utf-8"))

    path.unlink()  # 演示完删掉，保持目录干净
