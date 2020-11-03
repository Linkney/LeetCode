"""
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
"""

# 1 暴力双循环 n^2
# 2 快排加一趟遍历 nlogn + n


class Solution:
    # def findRepeatNumber(self, nums: List[int]) -> int:
    def findRepeatNumber(self, nums):
        nums.sort()
        for index in range(len(nums)):
            if nums[index] == nums[index+1]:
                return nums[index]
        return -1


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(Solution().findRepeatNumber(nums))

# 它考察的是程序员的沟通能力，先问面试官要时间/空间需求！！！
# 只是时间优先就用字典，
    #     def findRepeatNumber(self, nums):
    #         temp_set = set()
    #         repeat = -1
    #         for i in range(len(nums)):
    #             temp_set.add(nums[i])
    #             if len(temp_set) < i + 1:
    #                 repeat = nums[i]
    #                 break
    #         return repeat
# 还有空间要求，就用原地排序数组+指针

# 一个萝卜一个坑的想法,
# 因为题目里说明确说了要么不满足条件,要么是 range(0,n)的数组
# 依次给每个萝卜放回自己的坑
