# Again 2020年12月14日21:17:19 递归 + 逻辑短路
"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）

示例 1：
输入: n = 3
输出: 6

示例 2：
输入: n = 9
输出: 45
"""


# python的 and 操作如果最后结果为真，返回最后一个表达式的值，or 操作如果结果为真，返回第一个结果为真的表达式的值
class Solution:
    def sumNums(self, n: int) -> int:
        return n and (n + self.sumNums(n - 1))


class Solution2:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res


if __name__ == '__main__':
    print(0 and 1)
    print(0 and 2)
    print(1 and 0)
    print(1 and 2)
    print(2 and 1)
    print(0 and 0)
    # 第一个位置 0 则 0
    # 第一个位置 非0 则 取第二个数字
