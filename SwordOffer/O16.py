# Again 2020年11月9日10:18:56
"""
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

示例 1:
输入: 2.00000, 10
输出: 1024.00000

示例 2:
输入: 2.10000, 3
输出: 9.26100

示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
"""


# Python中的按位运算符有：左移运算符（<<），右移运算符（>>）,按位与（&），按位或（|），按位翻转（～）
# 这些运算符中只有按位翻转运算符是单目运算符，其他的都是双目运算符
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        # 数学特例
        if n == 0:
            return 1
        if x == 0:
            return 0

        else:
            # 负指数 转化为 正指数
            if n < 0:
                x = 1/x
                n = -n

            # 快速幂 （数学）   & 1 在判断 指数 的奇偶性 >> 1 即 指数 除二取整
            while n != 0:
                if (n & 1) == 1:
                    ans = ans * x
                x = x * x
                n = n >> 1
        return ans


if __name__ == '__main__':
    print(Solution().myPow(2.000, 10))
