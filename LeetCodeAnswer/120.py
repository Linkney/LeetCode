"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""


# def minimumTotal(self, triangle: List[List[int]]) -> int:
class Solution:
    def minimumTotal(self, triangle):
        # dp 从底下往上推   dp[i][j] = min( dp[i+1][j], dp[i+1][j+1] ) + dp[i][j]   Ans = dp[0][0]
        for row in range(len(triangle)-1, -1, -1):
            for col in range(len(triangle[row])-1, -1, -1):
                print('row:', row, ' col:', col)
                if row == len(triangle) - 1:
                    # 跳过最后一行
                    continue
                triangle[row][col] = triangle[row][col] + min(triangle[row+1][col], triangle[row+1][col+1])
        return triangle[0][0]


if __name__ == '__main__':
    Example = [
                 [2],
                [3,4],
               [6,5,7],
              [4,1,8,3]]
    s = Solution()
    ans = s.minimumTotal(Example)
    print("ans:", ans)
