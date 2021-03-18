# 这这.. 有限状态自动机
"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
"""


# 有限状态自动机
# 有一个特殊的状态，被称作「初始状态」。
# 还有一系列状态被称为「接受状态」，它们组成了一个特殊的集合。其中，一个状态可能既是「初始状态」，也是「接受状态」
# 起初，这个自动机处于「初始状态」。
# 随后，它顺序地读取字符串中的每一个字符，并根据当前状态和读入的字符，按照某个事先约定好的「转移规则」，
# 从当前状态转移到下一个状态；当状态转移完成后，它就读取下一个字符。当字符串全部读取完毕后，
# 如果自动机处于某个「接受状态」，则判定该字符串「被接受」；否则，判定该字符串「被拒绝」。
#
# 注意：如果输入的过程中某一步转移失败了，即不存在对应的「转移规则」，
# 此时计算将提前中止。在这种情况下我们也判定该字符串「被拒绝」。

# 状态 及 其对应的转移规则
# 输入一个字符 将 字符 转化成 转移规则
# 初始状态
# 判断是否 in 当前状态的转移规则里
#       不在 Return False
# 转移状态
# loop until 接收完全部字符
# 判断是否在接收态中
class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            {' ': 0, 's': 1, 'd': 2, '.': 4},  # 0. start with 'blank'
            {'d': 2, '.': 4},  # 1. 'sign' before 'e'
            {'d': 2, '.': 3, 'e': 5, ' ': 8},  # 2. 'digit' before 'dot'
            {'d': 3, 'e': 5, ' ': 8},  # 3. 'digit' after 'dot'
            {'d': 3},  # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            {'s': 6, 'd': 7},  # 5. 'e'
            {'d': 7},  # 6. 'sign' after 'e'
            {'d': 7, ' ': 8},  # 7. 'digit' after 'e'
            {' ': 8}  # 8. end with 'blank'
        ]

        # 状态码
        p = 0  # start with state 0

        for c in s:
            if '0' <= c <= '9':
                t = 'd'  # digit
            elif c in "+-":
                t = 's'  # sign
            elif c in "eE":
                t = 'e'  # e or E
            elif c in ". ":
                t = c  # dot, blank
            else:
                t = '?'  # unknown

            if t not in states[p]:
                return False

            p = states[p][t]
        # 接收态
        return p in (2, 3, 7, 8)


if __name__ == '__main__':
    s = "-1E-16"
    print(Solution().isNumber(s))
