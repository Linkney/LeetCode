"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序
请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数

示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
"""


# 从左到右  递增
# 从上到下  递增
class Solution:
    # def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
    def findNumberIn2DArray(self, matrix, target):
        # 以左下角 或者 右上角 为起点 flag
        #   若 target > flag 则 可以消去一列
        #   若 target < flag 则 可以消去一行
        x, y = len(matrix) - 1, 0
        while x >= 0 and y < len(matrix[0]):
            # print(x, y)
            if target > matrix[x][y]:
                y += 1
            elif target < matrix[x][y]:
                x -= 1
            else:
                return True
        return False

    def findNumberIn2DArray2(self, matrix, target):
        if len(matrix) == 0:
            # 防止 y = len(matrix[0]) 出问题
            return False
        x, y = 0, len(matrix[0]) - 1
        while x < len(matrix) and y >= 0:
            print(x, y)
            if target > matrix[x][y]:
                x += 1
            elif target < matrix[x][y]:
                y -= 1
            else:
                return True
        return False


if __name__ == '__main__':
    # matrix = [
    #           [1,   4,  7, 11, 15],
    #           [2,   5,  8, 12, 19],
    #           [3,   6,  9, 16, 22],
    #           [10, 13, 14, 17, 24],
    #           [18, 21, 23, 26, 30]
    #         ]
    matrix = [[-5]]
    target = -5
    print(Solution().findNumberIn2DArray(matrix, target))
    # print(Solution().findNumberIn2DArray2(matrix, target))

