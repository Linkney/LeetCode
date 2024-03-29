"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3]
输出: 2

示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
"""


# 二分法可以优化
class Solution:
    # def missingNumber(self, nums: List[int]) -> int:
    # 一趟遍历寻找
    def missingNumber(self, nums):
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

    # 二分法寻找
    def _missingNumber(self, nums):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i


if __name__ == '__main__':
    # nums = [0, 1, 3]
    # nums = [0, 1, 2, 3, 4, 5, 6, 7, 9]
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(Solution().missingNumber(nums))
