"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:
输入: [1,3,5,6], 2
输出: 1
示例 3:
输入: [1,3,5,6], 7
输出: 4
示例 4:
输入: [1,3,5,6], 0
输出: 0
"""

# def searchInsert(self, nums: List[int], target: int) -> int:
class Solution:
    def searchInsert(self, nums, target):

        i = 0
        # 递增序列 插入在 比他 大 的数字 前面  遇到相同  即 相当于 比他大
        while i < len(nums) and nums[i] < target:
            i = i + 1
        return i


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    print(Solution().searchInsert(nums, target))
