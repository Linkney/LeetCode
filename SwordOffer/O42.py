"""
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。

示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""


# 蛮力法：
#       1个 n种  2个 n-1种 ....  n个 1种
# 动态规划：
#       已知 [....] 最大值
#       求   [....X] 最大值
#       max( ....X ...X ..X .X X .....)
class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    # 暴力法
    def _maxSubArray(self, nums):
        # 数列求和函数
        def sum(nums):
            ans = 0
            for i in nums:
                ans += i
            return ans

        ans = nums[0]
        # 个数循环
        for numNum in range(1, len(nums)+1):
            # 起始下标循环
            for i in range(len(nums)):
                ans = max(ans, sum(nums[i:i+numNum]))

        return ans

    # 设动态规划列表 dp ，dp[i] 代表以元素 nums[i] 为结尾的连续子数组最大和
    # 若 dp[i-1] ≤ 0 ，说明 dp[i - 1] 对 dp[i] 产生负贡献
    # 即 dp[i-1] + nums[i] 还不如 nums[i] 本身大
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            # 要么带上 要么舍弃 孑然一身
            nums[i] += max(nums[i - 1], 0)
        return max(nums)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))

    # print(nums[1:2])
    # print(nums[7:22])
