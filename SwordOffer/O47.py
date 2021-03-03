"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物

示例 1:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
"""


# 动态规划
class Solution:
    # def maxValue(self, grid: List[List[int]]) -> int:
    def maxValue(self, grid):
        ans = [[0 for _ in range(len(grid[0])+1)] for __ in range(len(grid)+1)]
        # print(ans)
        for x in range(1, len(ans)):
            for y in range(1, len(ans[0])):
                # ↓ → 两个方向
                ans[x][y] = max(ans[x-1][y], ans[x][y-1]) + grid[x-1][y-1]

        # print(ans)
        return ans[-1][-1]


if __name__ == '__main__':
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    print(Solution().maxValue(grid))
