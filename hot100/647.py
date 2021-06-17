"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""


# 看 吃 逛 喝 散
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += self.expendCenter(s, i, i)
            ans += self.expendCenter(s, i, i+1)

        return ans

    # 由 left right 向外计算个数
    def expendCenter(self, s, left, right):
        ans = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            ans += 1
            left -= 1
            right += 1
        return ans


if __name__ == '__main__':
    # s = "aaa"
    s = "abs"
    print(Solution().expendCenter(s, 0, 0))
    print(Solution().expendCenter(s, 1, 1))
    print(Solution().expendCenter(s, 2, 2))
    print(Solution().expendCenter(s, 0, 1))
    print(Solution().expendCenter(s, 1, 2))
    print(Solution().expendCenter(s, 2, 3))
    print(Solution().countSubstrings(s))

