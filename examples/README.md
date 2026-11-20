# 学习路线（已确认）

确认日期：2026-11-20。顺序与范围已经本人确认，按此执行；要改动先说一声。

这个仓储一直用下去。每个阶段都在现有代码上加一层能力，不换项目，这样你能看到同一个东西怎么长大。

## 最终形态

核心六阶段学完后：一个小型网络模拟器——从真实数据源拉链路数据、按时延选最优路径、拓扑变化实时推给客户端。MySQL/Redis 是可选延伸，等主线走通、确实需要时再加。

## 起点（已掌握）

- 图用邻接表表示，`connect` / `disconnect` 维护双向边对称；
- BFS 用 `parent` 字典回溯路径，DFS 用显式栈加回溯；
- 8 个 pytest 用例，覆盖重复连接、重复断开、不可达、起终点相同、未知事件；
- `match` 事件分发，未知事件抛 `ValueError`；
- JSON：`loads` / `dumps`、字符串与字典的区别（练习 13 已过）。

## 核心六阶段（已确认顺序）

| 阶段 | 主题 | 交付物 | 扩展文件 | 状态 |
|---|---|---|---|---|
| 1 | JSON 数据处理 | 拓扑存文件、读回；从 API 形状数据拼拓扑 | 新增存取函数 | 进行中（13 过，14 待做） |
| 2 | Dijkstra + 优先队列 | 按总时延最小选路，说清与 BFS 跳数最少的区别 | `routing.py` | 未开始 |
| 3 | HTTP + requests | 从真实 API 拉链路数据，变成拓扑 | 新增抓取模块 + `main.py` | 未开始 |
| 4 | TCP / UDP + socket | 服务端/客户端互传拓扑，测往返时延 | 新增 socket 模块 | 未开始 |
| 5 | WebSocket | 拓扑一变，客户端立刻收到推送 | `simulation.py` 事件广播 | 未开始 |
| 6 | 收尾整合 | 接成能跑的小系统，补测试 | 全项目 | 未开始 |

## 可选延伸（暂不排期）

| 主题 | 交付物 |
|---|---|
| MySQL | `simulation.py` 的事件历史入库，按条件查询 |
| Redis | 缓存热点路径；发布订阅推送拓扑事件 |

## 为什么是这个顺序

1. JSON 放最前：它是后面每层的公共语言——HTTP 响应体、WebSocket 消息、MySQL 的 JSON 字段都用它。
2. Dijkstra 紧跟 BFS：只差两点——边带权重、用优先队列代替普通队列。趁 BFS 手感还在补最省力。
3. TCP/UDP 放在 WebSocket 前：WebSocket 本质是「HTTP 握手 + TCP 长连接」，先懂 socket 才不觉得是魔法。

主线一句话：数据能表示、能存（JSON）→ 算法更强（Dijkstra）→ 数据联网流动（HTTP→TCP/UDP→WebSocket）→ 落地存储（可选 MySQL/Redis）。

## 学习方式

每课三段，顺序不跳：

1. **跟读**：我写好完整代码，你运行、看输出、对照注释。对应 `examples/*_demo.py`。
2. **跟做**：改一两行，看输出怎么变。
3. **独立写**：才动手写新函数。对应 `examples/NN_*.py`，编号接着往下排。

约定：

- 一次只讲你能一次写完代码的规模。
- 你写完把代码和输出发我，我检查正确性、边界、命名；卡住给提示，尽量不直接贴答案。
- 每阶段结束先确认「这层过了」，再进下一层，不闷头往前赶。
- 阶段收尾把验证过的代码搬进 `topology.py` / `routing.py` / `simulation.py`，`examples/` 只是草稿本。

## 环境

统一到 `.venv`。系统 `python` 指向 conda 环境（`D:\.conda\envs\python_3.12`），没装 pytest；那 8 个测试是用 `.venv` 里的 pytest 跑的。

```powershell
.venv\Scripts\python.exe -m pytest -q
.venv\Scripts\python.exe -m pip install requests
```

VSCode 里 Ctrl+Shift+P → Python: Select Interpreter → 指到 `.venv\Scripts\python.exe`。否则阶段 3 装 requests 会装到错的环境。
