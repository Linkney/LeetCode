"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：
输入: s = "abcdefg", k = 2
输出: "cdefgab"

示例 2：
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:]+s[:n]

    # 字符串列表遍历 拼接    n ~ lens ~ 0 ~ n
    def reverseLeftWords2(self, s: str, n: int) -> str:
        res = []
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])
        return ''.join(res)

    # 字符串遍历 拼接
    def reverseLeftWords3(self, s: str, n: int) -> str:
        res = ""
        for i in range(n, n + len(s)):
            res += s[i % len(s)]
        return res
