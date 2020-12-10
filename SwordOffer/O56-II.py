"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次
请找出那个只出现一次的数字

示例 1：
输入：nums = [3,4,3,3]
输出：4

示例 2：
输入：nums = [9,1,7,9,7,9,7]
输出：1
"""


# 我选择原地裂开
class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    def singleNumber(self, nums):
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones


if __name__ == '__main__':
    nums = [9, 1, 7, 9, 7, 9, 7]
    print(Solution().singleNumber(nums))
