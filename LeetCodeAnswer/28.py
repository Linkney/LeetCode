"""
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，
在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""


class Solution:
    def checkSame(self, str1, str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
        return True

    def strStr(self, haystack: str, needle: str) -> int:
        # todo KMP ?
        # 滑动窗口
        windowLen = len(needle)
        textLen = len(haystack)
        if windowLen == 0:
            return 0
        if windowLen > textLen:
            return -1
        # 滑几隔
        cut = textLen - windowLen
        for i in range(cut + 1):
            if self.checkSame(haystack[i:i+windowLen], needle):
                return i
        return -1


