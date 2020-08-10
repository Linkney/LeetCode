"""
给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

示例 1:
输入: ["abcd","dcba","lls","s","sssll"]
输出: [[0,1],[1,0],[3,2],[2,4]]
解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2:
输入: ["bat","tab","cat"]
输出: [[0,1],[1,0]]
解释: 可拼接成的回文串为 ["battab","tabbat"]
"""


# def palindromePairs(self, words: List[str]) -> List[List[int]]:
class Solution:
    # 判断 word 是否为回文字符串
    def checkWord(self, word):
        for i in range(len(word)//2):
            if word[i] != word[len(word) - 1 - i]:
                return False
        return True

    # 将 word1 和 word2 的前后拼接 的 答案check 并记录进 ans
    def checkTwoWords(self, word1, index1, word2, index2, ans):
        word12 = word1 + word2
        if self.checkWord(word12):
            ans.append([index1, index2])
        word21 = word2 + word1
        if self.checkWord(word21):
            ans.append([index2, index1])
        return

    def palindromePairs(self, words):
        # 暴力法 每2个都拼接一次 然后验证    （超时）
        ans = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                self.checkTwoWords(words[i], i, words[j], j, ans)
        return ans


# 字典树
class Node:
    def __init__(self):
        self.ch = [0] * 26
        self.flag = -1


class Solution2:
    def palindromePairs(self, words):
        tree = [Node()]

        def insert(s: str, index: int):
            length = len(s)
            add = 0
            for i in range(length):
                x = ord(s[i]) - ord("a")
                if tree[add].ch[x] == 0:
                    tree.append(Node())
                    tree[add].ch[x] = len(tree) - 1
                add = tree[add].ch[x]
            tree[add].flag = index

        def findWord(s: str, left: int, right: int) -> int:
            add = 0
            for i in range(right, left - 1, -1):
                x = ord(s[i]) - ord("a")
                if tree[add].ch[x] == 0:
                    return -1
                add = tree[add].ch[x]
            return tree[add].flag

        def isPalindrome(s: str, left: int, right: int) -> bool:
            length = right - left + 1
            return length < 0 or all(s[left + i] == s[right - i] for i in range(length // 2))

        n = len(words)
        for i, word in enumerate(words):
            insert(word, i)

        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ret.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])

        return ret


if __name__ == '__main__':
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    # words = ["bat", "tab", "cat"]
    print(Solution().checkWord('abcddcba'))
    print(Solution().palindromePairs(words))
