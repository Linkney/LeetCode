"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

示例 1:
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2
"""


class Solution:
    def div(self, a, b):
        if a < b:
            # 如果被除数小于除数 商为 0
            return 0
        # 至少 商 有 1 了t
        count = 1
        tb = b
        # 除数翻倍 商翻倍
        while (tb + tb) <= a:
            count = count + count
            tb = tb + tb
        # 最大 翻倍 商  不能再 翻倍了    递归 调  被除数的残差
        return count + self.div(a-tb, b)

    def divide(self, dividend: int, divisor: int) -> int:
        # a / b = res …… x
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            # 这我人傻了啊  最小负数 和 最大正数 对应 -2147483648 ~ 0 ~ 2147483647
            if dividend == -2147483648:
                return 2147483647
            return -dividend

        # 仪表盘数值 初始化
        a, b = dividend, divisor
        sign = 1
        if ( a > 0 and b < 0 ) or ( a < 0 and b > 0 ):
            sign = -1
        a = abs(a)
        b = abs(b)

        res = self.div(a, b)

        return (res * sign)


