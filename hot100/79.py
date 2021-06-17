"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word
如果 word 存在于网格中，返回 true ；否则，返回 false
单词必须按照字母顺序，通过相邻的单元格内的字母构成
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
"""


class Solution:
    def exist(self, board, word):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # i j 坐标 k word 的 index
        def check(i, j, k):
            if board[i][j] != word[k]:
                return False

            # 在前一个 if 通过的前提 下 即 board[i][j] == work[k]
            if k == len(word) - 1:
                return True

            visited.add((i, j))

            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                # 如果在 范围内 且 还未被 visited 即 dfs 进入下一个阶段
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break

            # 一个 direction 一个 visited 回溯
            visited.remove((i, j))
            return result

        # 遍历起始位置 如果有一个可以通过 即 return True
        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    print(Solution().exist(board, word))
