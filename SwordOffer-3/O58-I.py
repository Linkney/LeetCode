"""
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变
为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

示例 1：
输入: "the sky is blue"
输出: "blue is sky the"

示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()  # 删除首尾空格
        strs = s.split()  # 分割字符串
        strs.reverse()  # 翻转单词列表
        return ' '.join(strs)  # 拼接为字符串并返回

    # 双指针
    def reverseWords2(self, s: str) -> str:
        s = s.strip()  # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1  # 搜索首个空格
            res.append(s[i + 1: j + 1])  # 添加单词
            while s[i] == ' ': i -= 1  # 跳过单词间空格
            j = i  # j 指向下个单词的尾字符
        return ' '.join(res)  # 拼接并返回

