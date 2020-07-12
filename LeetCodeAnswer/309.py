"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

"""


# def maxProfit(self, prices: List[int]) -> int:
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        # 公理1： 表格包含了所有时间截面的情况
        # 公理2： 转移情况正确   f[x][y] 在 x 天 y 状态 下的最大收益
        # 遍历 剪枝
        n = len(prices)
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期（明天是冷冻）中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期（明天是冷冻）中的累计最大收益
        f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        print(f)

        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            f[i][1] = f[i - 1][0] + prices[i]
            f[i][2] = max(f[i - 1][1], f[i - 1][2])

        print(f)
        return max(f[n - 1][1], f[n - 1][2])


if __name__ == '__main__':
    Example = [1, 2, 3, 0, 2]
    s = Solution()
    print(s.maxProfit(Example))
