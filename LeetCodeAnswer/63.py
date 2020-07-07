# 63. 不同路径 II
# 输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2

"""
 动态规划 d[i][j] = d[i-1][j] + d[i][j-1]
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        print(obstacleGrid)
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            row = len(obstacleGrid)
            col = len(obstacleGrid[0])
            # 形状左上大一圈的 答案模板 list_three = [[0 for i in range(3)] for j in range(3)]
            ansTable = [[0 for i in range(col+1)] for j in range(row+1)]
            print(ansTable)
            # 起点 的 左边 或者 上面 来个 1 即可
            ansTable[0][1] = 1
            print(ansTable)
            # 一列一列 写
            for x in range(row):
                for y in range(col):
                    # 从 obstacleGrid[x][y] 0/1信息 来填写 ansTable[x+1][y+1] 中的路径条数
                    if obstacleGrid[x][y] == 1:
                        print('x:', x, 'y:', y, ' 障碍')
                        # 该点是障碍 走到该位置的 路径数 为 0
                        ansTable[x+1][y+1] = 0
                    else:
                        # 正常 左 + 上
                        print('x:', x, 'y:', y, ' 通路')
                        ansTable[x+1][y+1] = ansTable[x][y+1] + ansTable[x+1][y]
            print(ansTable)
            return ansTable[row][col]


if __name__ == '__main__':
    example = [[0, 0, 0],
               [0, 1, 0],
               [0, 0, 0]]

    s = Solution()
    ans = s.uniquePathsWithObstacles(example)
    print('Ans：', ans)


