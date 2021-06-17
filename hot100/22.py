"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]
"""


class Solution:
    def generateParenthesis(self, n):
        ans = []

        # 如果左括号数量不大于 nn，我们可以放一个左括号。如果右括号数量小于左括号的数量，我们可以放一个右括号

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return

            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()

            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans


class Solution2:
    def generateParenthesis(self, n):
        # (parentheses, #left, #right)
        stack = [('', 0, 0)]
        ans = []
        while stack:
            p, left, right = stack.pop()
            if left == right == n:
                ans.append(p)
                continue

            if left < n:
                stack.append((p + '(', left + 1, right))
            if right < n and right < left:
                stack.append((p + ')', left, right + 1))
        return ans


from typing import List


# 回溯 DFS
class Solution3:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res


if __name__ == '__main__':
    print(Solution3().generateParenthesis(2))

