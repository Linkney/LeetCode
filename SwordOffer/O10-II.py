"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：n = 2
输出：2
示例 2：
输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1
"""


# 介不是一样 (n) = (n-1) + (n-2)
class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        a, b = 1, 1     # 0, 1  -->   1, 2   -->  2, 3 ....
        for _ in range(n):
            a, b = b, a+b
        return a % 1000000007


if __name__ == '__main__':
    n = 7
    print(Solution().numWays(7))
