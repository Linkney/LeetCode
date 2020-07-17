"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 双向扫描 左 到 右    需要 ) 来匹配 (    右到左 需要 ( 来匹配 )
        max_length = 0
        length = 0
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left = left + 1
            else:
                right = right + 1
            print('判断字符串后  left:', left, '  right:', right)
            if right == left:
                length = right * 2
                max_length = max(max_length, length)
                print('有效长度  length:', length)
            if left < right:
                right = 0
                left = 0
            print('决策大小关系后  left:', left, '  right:', right)

        length = 0
        left = 0
        right = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                right = right + 1
            else:
                left = left + 1
            if right == left:
                length = right * 2
                max_length = max(max_length, length)
            if right < left:
                right = 0
                left = 0

        return max_length


if __name__ == '__main__':
    s = '()((())'
    print(Solution().longestValidParentheses(s))
