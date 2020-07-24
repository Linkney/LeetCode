"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""


# def minPathSum(self, grid: List[List[int]]) -> int:
class Solution:
    def pprint(self, grid):
        for i in grid:
            print(i)
        print("----------------------")

    def minPathSum(self, grid):
        # 动态规划入门题
        # 答案模板复制
        ans = [[0 for _ in range(len(grid[0]))] for __ in range(len(grid))]
        self.pprint(ans)
        # 基础信息初始化  dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        ans[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            ans[i][0] = ans[i-1][0] + grid[i][0]
        for i in range(1, len(grid[0])):
            ans[0][i] = ans[0][i-1] + grid[0][i]
        self.pprint(ans)
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                ans[row][col] = min(ans[row-1][col], ans[row][col-1]) + grid[row][col]
        self.pprint(ans)
        return ans[-1][-1]


if __name__ == '__main__':
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1],
            [4,2,1]]
    print(Solution().minPathSum(grid))
