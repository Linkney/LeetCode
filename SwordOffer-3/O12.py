# Again 2020年11月4日21:25:33  DFS
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
        # finishIndex = len(word) - 1

        def dfs(x, y, indexOfWord):
            if x < 0 or y < 0 or x > len(board) - 1 or y > len(board[0]) - 1:
                return False
            if board[x][y] != word[indexOfWord]:
                return False
            # print("     内部dfs： ", x, y, word[indexOfWord])
            if indexOfWord == len(word) - 1:
                return True
            tmp = board[x][y]
            board[x][y] = '/'
            ans = dfs(x-1, y, indexOfWord+1) or dfs(x+1, y, indexOfWord + 1) \
                  or dfs(x, y-1, indexOfWord + 1) or dfs(x, y+1, indexOfWord + 1)
            # 该dfs失败了 恢复迷宫原状
            board[x][y] = tmp
            return ans

        for x in range(0, len(board)):
            for y in range(0, len(board[x])):
                print("外围双For循环： ", x, y)
                if dfs(x, y, 0):
                    return True

        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(Solution().exist(board, word))
