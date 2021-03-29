# Again 2020年11月4日21:31:12   BFS
"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3
示例 2：
输入：m = 3, n = 1, k = 0
输出：1
"""
from queue import Queue


# _________                      ____
# _________     Queue    →     |___|   Set    想象那个广搜的过程
# 数位和
def digitsum(n):
    ans = 0
    # n > 0, n 取余, n 除 10 取整
    while n:
        ans += n % 10
        n = n // 10
    return ans


# 矩阵广搜搜索 + 将 大于K的 看做障碍
class Solution:
    def movingCount(self, m, n, k):
        # 从 [0, 0] 开始移动 这个非常的关键
        queue = Queue()
        queue.put((0, 0))
        # ans = set()
        ans = []
        appearInQueue = set()
        orderX = [1, 0]      # orderX = [-1, 1, 0, 0]
        orderY = [0, 1]      # orderY = [0, 0, 1, -1]
        while not queue.empty():
            # 队列中的 x, y 保证必然在 矩阵范围内 且 0,0 可达
            x, y = queue.get()
            if (digitsum(x) + digitsum(y)) <= k:
                # ans.add((x, y))
                ans.append('duang')
                for i in range(2):
                    xTemp = x + orderX[i]
                    yTemp = y + orderY[i]
                    # 可能重复入队
                    if 0 <= xTemp < m and 0 <= yTemp < n and (xTemp, yTemp) not in appearInQueue:
                        queue.put((xTemp, yTemp))
                        appearInQueue.add((xTemp, yTemp))
                        # print(xTemp, yTemp)
        return len(ans)

    def movingCount2(self, m, n, k):
        # 工具人队列  存可以走到的位置 （待 check）
        q = Queue()
        q.put((0, 0))
        # 存可行位置集合
        s = set()
        while not q.empty():
            # 队列不为空 取出坐标
            x, y = q.get()
            # 符合规则 且 不在 可行set中
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) + digitsum(y) <= k:
                s.add((x, y))
                # 将两个 → ↓ 两个广搜方向 加入 待测试队列中
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    q.put((nx, ny))
                    # print(nx, ny)
        # 待测试队列为空时 就得到答案了
        return len(s)


if __name__ == '__main__':
    m = 36
    n = 11
    k = 15
    print(Solution().movingCount(m, n, k))
    # print(Solution().movingCount2(m, n, k))

    # q = Queue()
    # q.put(1)
    # print(q.empty())
    # print(q.get())
    # print(q.empty())