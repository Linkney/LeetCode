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
        # todo 2021年3月16日22:59:14


        return -1


if __name__ == '__main__':
    m = 2
    n = 3
    k = 1
    print(Solution().movingCount(m, n, k))
