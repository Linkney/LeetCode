"""
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
"""


class Solution:
    # def findRepeatNumber(self, nums: List[int]) -> int:
    # 排序
    def findRepeatNumber(self, nums):
        nums.sort()
        for index in range(len(nums)):
            if nums[index] == nums[index+1]:
                return nums[index]
        return -1

    # 萝卜坑
    def findRepeatNumber2(self, nums):
        # 0 ~ n-1 有重复 就 有缺失
        # 一遍遍历 将 x 放到 index 对应 位置  假设 无重复
        index = 0       # 要 将该位置上的数字 放到其对应位置上去   0,1,...
        while index < len(nums):
            # print(index)
            if index != nums[index]:
                # print(nums)
                # 调换位置   nums[index]   <-->   nums[nums[index]]
                if nums[nums[index]] == nums[index]:
                    # 发生冲突
                    return nums[index]
                temp = nums[nums[index]]
                nums[nums[index]] = nums[index]
                nums[index] = temp
                # nums[nums[index]], nums[index] = nums[index], nums[nums[index]]   # 这个可以  本质上和 写 temp 一样
                # nums[index], nums[nums[index]] = nums[nums[index]], nums[index]   # 这个不行
            else:
                # 该位置已经弄好
                index += 1
        return -1

    # HashTable
    def findRepeatNumber3(self, nums):
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return num
            hashmap[num] = 1
        return -1


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]

    # print(Solution().findRepeatNumber(nums))
    # print(Solution().findRepeatNumber2(nums))
    print(Solution().findRepeatNumber3(nums))
