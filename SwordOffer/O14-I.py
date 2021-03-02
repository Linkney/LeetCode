"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1）
每段绳子的长度记为 k[0],k[1]...k[m-1]
请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
"""


# 貌似递推
# 绳子长度 (1)  2  3  4  5  6  7   8    9.....  10
# 最大乘积 (1)  1  2  4  6  9
# max      (1)  2  3  4  6  9  12  18   27      36
# m = x + y    x 和 y 各自有各自的最大乘积   f(m) = f(x) * f(y)
# m 能得到的最大乘积 = max[（1,m-1) (2,m-2) ... (m/2, m/2)]
class Solution:
    def cuttingRope(self, n: int) -> int:
        # 简单情况
        if n <= 3:
            return n-1
        # 初始情况
        ans = [-1 for _ in range(n+1)]
        ans[1] = 1
        ans[2] = 2
        ans[3] = 3
        # print(ans)

        for index in range(4, n+1):
            # print("index:", index)
            # print(ans)
            for i in range(1, index):
                # print("i:", i, "index:", index, "ans[i[:", ans[i], ",  ans[index-i]:", ans[index-i])
                ans[index] = max(ans[i]*ans[index-i], ans[index])
        return ans[n]


if __name__ == '__main__':
    print(Solution().cuttingRope(10))
