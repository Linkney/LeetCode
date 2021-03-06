"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution:
    def numTrees(self, n: int) -> int:
        # G(n) 表示 以 1, 2, ..., n 为 节点的二叉搜索树的种数
        # F(i, n) 表示 以 i 为根节点的 1, 2, ..., n 的二叉搜索树的种数
        # G(n) = F(i, n) 【i 从 1, 2, ...n 求和】
        # F(i, n) = G(i-1) * G(n-i) 左右子树的种数的笛卡尔积
        # 由 上面两式 可得 G(n) = G(i-1) * G(n-i) 【i 从1, 2, ..n 求和】
        # 其中 启动特例为 G(0) = 1, G(1) = 1, G(2) = 2

        # 答案数组 0 1 2 ... n 下标
        G = [0] * (n + 1)

        G[0], G[1] = 1, 1

        for i in range(2, n + 1):
            # 从下标 2 开始填答案 直到 下标 n   i 即 下标  i 即 G(n)
            for j in range(1, i + 1):
                # G(n) = G(i-1) * G(n-i) 【i 从1, 2, ..n 求和】（此时 n = 上层循环里的 i)    j 从 1, .., i
                G[i] = G[i] + G[j - 1] * G[i - j]

        # 对应数学问题 卡塔兰数  可得数列首项和数列递推公式
        return G[n]

