"""
给定一个字符串 s 和一些长度相同的单词 words。
找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1：
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

示例 2：
输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
"""

from collections import Counter


# def findSubstring(self, s: str, words: List[str]) -> List[int]:
class Solution:
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        one_word = len(words[0])
        all_len = len(words) * one_word

        n = len(s)
        words = Counter(words)

        print(words)

        res = []
        print('n:', n, 'all_len:', all_len)
        # 滑动窗口
        for i in range(0, n - all_len + 1):
            # 当前 i 开始的窗口
            tmp = s[i:i + all_len]
            print(tmp)
            c_tmp = []
            for j in range(0, all_len, one_word):
                # 按照 单词长度 划分 小窗口 检测
                c_tmp.append(tmp[j:j + one_word])
                print(c_tmp)
            # 即 相等 数量 相等  次序无关
            if Counter(c_tmp) == words:
                res.append(i)

        return res


if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    sol = Solution()
    print(sol.findSubstring(s, words))
