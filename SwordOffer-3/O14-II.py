# Again 2020年11月5日17:23:41
"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
"""


# 缓缓打出 ?
# 结果需要取余 dp 中间结果不对劲
# 绳子长度 (1)  2  3  4  5  6  7   8    9.....  10
# 最大乘积 (1)  1  2  4  6  9
# max      (1)  2  3  4  6  9  12  18   27      36
# 拆解到 3
# 数学证明：
#           驻点 = 2.7

# 切分规则:
# 最优： 3  把绳子尽可能切为多个长度为 3 的片段，留下的最后一段绳子的长度可能为 0,1,2 三种情况。
# 次优： 2  若最后一段绳子长度为 2 ；则保留，不再拆为 1+1 。
# 最差： 1  若最后一段绳子长度为 1 ；则应把一份 3 + 1 替换为 2 + 2，因为 2×2 > 3×1


class Solution:
    def cuttingRope(self, n: int) -> int:
        # 简单情况
        if n <= 3:
            return n-1

        res = 1
        while n > 4:
            res *= 3
            res = res % 1000000007
            n -= 3
        return res * n % 1000000007


if __name__ == '__main__':
    print(Solution().cuttingRope(10))
