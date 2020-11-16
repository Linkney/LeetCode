"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,  3, 4],
                 [5,6,  7, 8],
                 [9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return 0

        ans = []
        # 0,0 --> 0, col  --> row, col --> row, 0  --> 1, 0  -->  loop
        # loop 调用 顺时针转一圈 smaller 矩阵

        # 起点 0, 0
        # 方向舵 [x, y]
        order = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # 长度舵 (从 -1,0开始 前进经过的数字数 行列均为个数)
        #  列    -->  行-1  -->  列-1  -->  行-2
        #  列-2       行-3       列-3       行-4        -2
        line = [len(matrix[0]), len(matrix)-1, len(matrix[0])-1, len(matrix)-2]

        x = 0
        y = -1
        indexLine = 0       # 0 1 2 3
        indexOrder = 0      # 0 1 2 3
        turn = 0
        while line[indexLine] > 0:
            print("turn:{}".format(turn))
            print("line:", line)
            for _ in range(line[indexLine]):

                x += order[indexOrder][0]
                y += order[indexOrder][1]
                print("x:{}, y:{}".format(x, y))
                ans.append(matrix[x][y])
                print(ans)

            indexOrder = (indexOrder + 1) % 4
            indexLine = (indexLine + 1) % 4
            turn += 1
            if turn % 4 == 0 and turn > 0:
                # 4 次 一削减
                line = [(i - 2) for i in line]
                print("Cut line:", line)

        return ans

    def clearSpiralOrder(self, matrix):
        ans = []
        order = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        line = [len(matrix[0]), len(matrix)-1, len(matrix[0])-1, len(matrix)-2]
        x = 0
        y = -1
        index = 0

        while line[index] > 0:
            for _ in range(line[index]):
                x += order[index][0]
                y += order[index][1]
                ans.append(matrix[x][y])
            index = index + 1
            if index == 4:
                index = 0
                line = [(i - 2) for i in line]
        return ans


if __name__ == '__main__':
    # matrix = [[1, 2, 3],
    #           [4, 5, 6],
    #           [7, 8, 9]]
    # matrix = [[1, 2, 3, 4],
    #           [5, 6, 7, 8],
    #           [9, 10, 11, 12]]
    matrix = [[1,   2,  3,  4,  5],
              [6,   7,  8,  9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]
    print(Solution().clearSpiralOrder(matrix))
