"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."
"""


class Solution:
    # def replaceSpace(self, s: str) -> str:
    def replaceSpace(self, s):
        ans = ''
        for item in s:
            if item == ' ':
                ans += "%20"
                continue
            ans += item
        return ans

    def replaceSpace2(self, s):
        return s.replace(" ", "%20")


if __name__ == '__main__':
    s = "We are happy."
    print(Solution().replaceSpace2(s))
