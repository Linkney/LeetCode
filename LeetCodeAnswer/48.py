"""
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


# def rotate(self, matrix: List[List[int]]) -> None:
class Solution:
    def pprint(self, m):
        for i in m:
            print(i)
        print('------------')

    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 第一行变成最后一列   第 i 行 变成 第 ( N - i ) 列
        #  i, j 到  j, N - i （公式）
        # 先转置 在镜像翻转
        # 四角螺旋转转转  （Tips： 就地 in-place 不是指就不能用其他任意一点点的额外空间了）
        N = len(matrix)
        self.pprint(matrix)

        for i in range(N // 2 + N % 2):

            for j in range(N // 2):
                print(i, j)

                tmp = matrix[N - 1 - j][i]
                # 变量代换 （公式）
                matrix[N - 1 - j][i] = matrix[N - 1 - i][N - j - 1]
                matrix[N - 1 - i][N - j - 1] = matrix[j][N - 1 - i]
                matrix[j][N - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp

                self.pprint(matrix)



if __name__ == '__main__':
    matrix =[[5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]]
    Solution().rotate(matrix)
