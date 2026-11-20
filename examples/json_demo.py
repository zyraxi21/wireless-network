"""第 1 课（跟读）：JSON 是什么，json 模块怎么用。

这个文件已经全部写好，你只需要运行，然后对照注释看输出：

    .venv\\Scripts\\python.exe lessons\\lesson01_demo.py

建议顺序：先完整跑一遍，再回头一节一节看。
"""

import json
from pathlib import Path


def section(title):
    """打印一个醒目的分节标题，方便把输出和代码对上。"""
    print()
    print("-" * 62)
    print(title)
    print("-" * 62)


network = {"A": ["B", "C"], "B": ["A"]}
zh = {"节点A": ["节点B"], "节点B": ["节点A"]}


# ================================================================ 第 1 节
section("第 1 节  看清两个世界：内存里的对象，和网络上的文本")

print("network 是：", network)
print("它的类型是：", type(network))

# 注意上面输出里是单引号 'A'。这在 Python 里合法，在 JSON 里不合法。
# 所以 Python 对象不能直接塞进网络，必须转成 JSON 文本。


# ================================================================ 第 2 节
section("第 2 节  dumps：对象 -> 字符串")

text = json.dumps(network)
print("dumps 的结果：", text)
print("结果的类型：", type(text))
print("结果的长度：", len(text))

# 观察：单引号全部变成了双引号，而且现在它只是一个普通的 str。
# dumps 里的 s 就是 string，意思是「转成字符串」。


# ================================================================ 第 3 节
section("第 3 节  loads：字符串 -> 对象")

back = json.loads(text)
print("loads 的结果：", back)
print("结果的类型：", type(back))

# == 比的是内容，is 比的是「是不是同一个东西」
print("内容和原来一样吗：", back == network)
print("是同一个对象吗：  ", back is network)

# loads 每次都造出一个新对象。这点很重要：读回来的东西和原来的互不影响。


# ================================================================ 第 4 节
section("第 4 节  三个必须用的参数")

# 参数一：ensure_ascii。默认 True，会把中文转成 \uXXXX
print("默认：      ", json.dumps(zh))
print("关掉转义：", json.dumps(zh, ensure_ascii=False))

# 参数二：indent。默认挤成一行，加缩进后能看结构
print("默认：")
print(json.dumps(network))
print("加缩进：")
print(json.dumps(network, indent=2))

# 参数三：sort_keys。不加时，输出顺序跟着字典的插入顺序走
print("不排序：", json.dumps({"B": [], "A": []}))
print("排序：  ", json.dumps({"B": [], "A": []}, sort_keys=True))
print("另一种构造顺序，加了 sort_keys 后输出一样：")
print(json.dumps({"A": [], "B": []}, sort_keys=True))


# ================================================================ 第 5 节
section("第 5 节  存进文件，再读回来")

path = Path(__file__).with_name("_demo_topology.json")

# dump（没有 s）第一个参数是对象，第二个参数是文件对象
with path.open("w", encoding="utf-8") as f:
    json.dump(zh, f, ensure_ascii=False, indent=2)

print("文件里现在是这样的：")
print(path.read_text(encoding="utf-8"))

# load（没有 s）直接从文件对象里读
with path.open(encoding="utf-8") as f:
    loaded = json.load(f)
print("从文件读回来：", loaded)
print("和原来一样吗：", loaded == zh)

# 故意用 GBK 去读这个 UTF-8 文件，看看会发生什么
try:
    print("用 GBK 读：", path.read_bytes().decode("gbk"))
except UnicodeDecodeError as error:
    print("用 GBK 读直接报错：", error)

print("为什么？写的时候用 UTF-8，读的时候就必须用 UTF-8，两边要一致。")
print("Windows 的默认编码是 GBK，所以 encoding='utf-8' 每次都要显式写。")

path.unlink()  # 演示完删掉，保持目录干净


# ================================================================ 第 6 节
section("第 6 节  三个坑，提前踩一次")

# 坑一：JSON 的键只能是字符串
sneaky = {1: "A", 2: "B"}
print("原始字典：", sneaky)
after = json.loads(json.dumps(sneaky))
print("过一遍 JSON：", after)
print("1 还在吗：", 1 in after, " '1' 在吗：", "1" in after)

# 坑二：NaN 不是合法 JSON，但 Python 默认会放行
print("默认会写出：", json.dumps({"x": float("nan")}))
try:
    json.dumps({"x": float("nan")}, allow_nan=False)
except ValueError as error:
    print("加上 allow_nan=False 就拦住了：", error)

# 坑三：JSON 不是 Python 字面量，单引号和尾随逗号都不认
for bad in ["{'a': 1}", '{"a": 1,}', '{"a": 1}']:
    try:
        json.loads(bad)
        print(bad, "-> 合法的 JSON")
    except json.JSONDecodeError:
        print(bad, "-> 解析失败，不是合法 JSON")


# ================================================================ 第 7 节
section("第 7 节  真实数据长什么样（阶段 3 就是拿这种数据）")

payload = {
    "network": {
        "nodes": ["A", "B", "C"],
        "links": [
            {"source": "A", "target": "B", "latency_ms": 12},
            {"source": "B", "target": "C", "latency_ms": 8},
        ],
    }
}

print("三层嵌套，取值就是一层层往里走：")
print("  payload['network']['nodes'] ->", payload["network"]["nodes"])

print("遍历链路表：")
for link in payload["network"]["links"]:
    print("  ", link["source"], "到", link["target"], "时延", link["latency_ms"], "ms")

total = sum(link["latency_ms"] for link in payload["network"]["links"])
print("所有时延加起来：", total, "ms")


# ================================================================ 第 8 节
section("第 8 节  跟做：改三处，再跑一次")

print("下面三件事由你来做，改完重新运行这个文件，看输出哪里变了。")
print()
print("  1. 第 4 节，把 indent=2 改成 indent=4，看缩进变宽。")
print("  2. 第 4 节，给 zh 加一个孤儿节点：zh = {'节点A': ['节点B'], '节点B': ['节点A'], '节点C': []}")
print("     然后再看 ensure_ascii=False 那一行，多出来的空列表长什么样。")
print("  3. 第 7 节，把 total 那行改成只统计 source 是 'A' 的时延。")
print("     提示：在 for 循环里加 if，或者用 sum 后面的表达式加条件。")
print()
print("改坏了不要紧，这个文件可以随时恢复。")

section("跟读结束")
print("三个改动都做完、输出都看懂了，再打开 lesson01_json.py 做独立练习。")
