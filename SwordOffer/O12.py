# Again 2020年11月4日21:25:33  DFS
#
"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格
那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

示例 1：
输入：board = [["A","B","C","E"],
               ["S","F","C","S"],
               ["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["a","b"],
               ["c","d"]], word = "abcd"
输出：false
"""


# 矩阵搜索
class Solution:
    # def exist(self, board: List[List[str]], word: str) -> bool:
    def exist(self, board, word):
        def dfs(i, j, k):
            # i, j 迷宫中的位置坐标 k word 中在 Check 的坐标
            # 坐标越界 or word 不对应
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            # 坐标合规 且 word 匹配
            print("     内部dfs： ", i, j, word[k])
            if k == len(word) - 1:
                return True
            # 已用迷宫格子 画×
            tmp, board[i][j] = board[i][j], '/'
            # 上下左右
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # 该dfs失败了 恢复迷宫原状
            board[i][j] = tmp
            return res

        # 矩阵遍历
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(Solution().exist(board, word))
