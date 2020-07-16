"""
给定一个无向图graph，当这个图为二分图时返回true。
如果我们能将一个图的节点集合分割成两个独立的子集A和B，
并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。
每个节点都是一个在0到graph.length-1之间的整数。
这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。

示例 1:
输入: [[1,3], [0,2], [1,3], [0,2]]
输出: true
解释:
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。

示例 2:
输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
输出: false
解释:
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。
"""

import collections


# def isBipartite(self, graph: List[List[int]]) -> bool:
class Solution:
    def isBipartite(self, graph):
        # 染色 红 绿 二分  红 连接 绿  绿 连接  红

        # 仪表盘 ： 1 节点的对应 颜色
        #           2 染色剂颜色
        #           3 节点队列通道
        # 算法逻辑：染色  入队  出队  遍历  邻接 节点
        #           并 染色 入队  若 已经 染色 判断 颜色 是否和当前染色剂颜色相同

        # 节点数
        n = len(graph)

        UNCOLORED, RED, GREEN = 0, 1, 2

        # 节点的上色信息
        color = [UNCOLORED] * n

        for i in range(n):
            if color[i] == UNCOLORED:
                # 队列 [] 里 放入 第 i 个节点 该节点标记为 红色
                q = collections.deque([i])
                color[i] = RED
                # 只要队列里不为空  即  对 已经染色的 节点的 广搜没有全部完成
                while q:
                    # 首元素 出队
                    node = q.popleft()
                    # 如果该 节点为 红色 那么 染色剂 为 绿色   染色剂 颜色  与 该节点颜色  置 反
                    cNei = (GREEN if color[node] == RED else RED)
                    # 邻接节点遍历
                    for neighbor in graph[node]:
                        # 未染色 的 染色 入队
                        if color[neighbor] == UNCOLORED:
                            q.append(neighbor)
                            color[neighbor] = cNei
                        # 已染色 的 判断 颜色
                        elif color[neighbor] != cNei:
                            return False
        return True


if __name__ == '__main__':
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(Solution().isBipartite(graph))
