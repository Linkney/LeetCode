"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。

示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        # SUM = x + y + z + ...         Mut = x * y * z * ...
        # 数学        拆分出尽可能多的 3   函数极值 或者 归纳证明法
        if n <= 3:
            return n - 1

        quotient, remainder = n // 3, n % 3
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        else:
            return 3 ** quotient * 2

    def _integerBreak(self, n: int) -> int:
        # 动态规划
        # dp[k] 表示 将 k 数字拆成2个及以上正整数时候 乘积最大的值
        # dp[k] = max ( dp[k-x] * dp[x] )     x from 0 to k-1  遍历 拆分
        # 初始化的值： dp[0] = 0    dp[1] = 0      dp[2] = 1    dp[3] = 2
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                # max（ 本身记忆 ， 拆出一个数后2数相乘 ， 拆出一个数后 数dp相乘 )
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]
