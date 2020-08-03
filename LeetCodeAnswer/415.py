"""

给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：
num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 非负 字符串 整数    计算和
        index1 = len(num1) - 1
        index2 = len(num2) - 1
        ans = 0
        # 进位缓存器
        add = 0
        # 位数缓存器
        digits = 1
        # 两个指针都走到  数字最高位  字符串数据[0]  位置   或者 进位计数器里还有数
        while index1 >= 0 or index2 >= 0 or add == 1:
            # 每次循环计算一位数据  拨动 进位缓存 和 位数缓存
            tempnum1 = ord(num1[index1]) - ord('0') if index1 >= 0 else 0
            tempnum2 = ord(num2[index2]) - ord('0') if index2 >= 0 else 0

            print(index1, index2, tempnum1, tempnum2)
            # 该数位求和
            tempnum = tempnum1 + tempnum2 + add

            add = 0
            if tempnum > 10:
                tempnum = tempnum - 10
                add = 1
            ans = ans + tempnum * digits

            digits = digits * 10
            index1 = index1 - 1
            index2 = index2 - 1

        return str(ans)


if __name__ == '__main__':
    # num1 = '86043'
    # num2 = '5582'
    num1 = '9'
    num2 = '9'
    print(Solution().addStrings(num1, num2))
