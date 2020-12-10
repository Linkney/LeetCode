"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s
如果有多对数字的和等于s，则输出任意一对即可

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

示例 2：
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
"""


# 双循环暴力 + 剪枝
# 对撞双指针
#       正确性证明
#               一共有 N * N 个组组合 每次 移动一个指针 实际上 划掉了 N 个组合
class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        for small in range(len(nums)-1):
            # if nums[small] + nums[small+1] > target:
            #     break
            # print("Small:", small)
            for lager in range(small+1, len(nums)):
                # print("Big:", lager)
                if nums[small] + nums[lager] > target:
                    break
                if nums[small] + nums[lager] == target:
                    return [nums[small], nums[lager]]

        return None

    def twoSum2(self, nums, target):
        small, big = 0, len(nums) - 1
        while small < big:
            s = nums[small] + nums[big]
            if s > target:
                big -= 1
            elif s < target: 
                small += 1
            else:
                return [nums[small], nums[big]]
        return []


if __name__ == '__main__':
    # nums = [2, 7, 11, 15]
    # target = 9
    nums = [10, 26, 30, 31, 47, 60]
    target = 40
    print(Solution().twoSum(nums, target))
    print(Solution().twoSum2(nums, target))
