"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


# def searchRange(self, nums: List[int], target: int) -> List[int]:
class Solution:
    def extreme_insertion_index(self, nums, target, left):
        # 二分查找
        lo = 0
        hi = len(nums)

        while lo < hi:
            # 除二取整
            mid = (lo + hi) // 2
            # True：中值 大于 或者 等于 目标值   中值位置 为 hi  但 不返回 使之往左靠  直到到 最左边的目标值
            # 才会触发 while 的退出机制    lo hi 相邻情况
            # False：中值 大于 目标值  中值位置 为 hi
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            # True： 中值 小于 目标值 中值位置 + 1 为 lo
            # False： 中值  小于 或 等于 目标值  中值位置 + 1 为 lo  但 不返回 使之往右靠  直到到 最右边的目标值
            else:
                lo = mid + 1
        return lo

    def searchRange(self, nums, target):
        # 返回最左边的target 的 index
        left_idx = self.extreme_insertion_index(nums, target, True)

        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]

