# Again 位运算 （不想看）
"""
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

示例:
输入: a = 1, b = 1
输出: 2
"""


#     a     b     和     进位和
#     0     0     0      0
#     1     0     1      0
#     0     1     1      0
#     1     1     0      1
# 和          a ^ b  异或运算
# 进位和      a & b  与运算
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)

    # 简单清晰！
    def add2(self, a, b):
        if b == 0:
            return a

        return self.add2(a ^ b, (a & b) << 1)


if __name__ == '__main__':
    a = 6
    b = 4
    print(Solution().add(a, b))
    print(Solution().add2(a, b))
