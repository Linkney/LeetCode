'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
'''


class Solution:
    def expend(self, nums, index, target):
        print("In expend index:{}".format(index))
        # return [start, end]
        start, end = index, index

        # <--
        while start >= 0 and nums[start] == target:
            start -= 1
        # ==>
        while end <= (len(nums) - 1) and nums[end] == target:
            end += 1
        return [start + 1, end - 1]

    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]

        # 升序排列 有重复元素
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            print("Index of left:{}, mid:{}, right:{}".format(left, mid, right))
            if nums[mid] == target:
                # from mid
                return self.expend(nums, mid, target)

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if nums[left] == target:
            return [left, left]
        else:
            return [-1, -1]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums, target))
    # 居合斩
