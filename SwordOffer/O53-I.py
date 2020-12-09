"""
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
"""


# 二分法找到数字 然后 先后推进统计 个数
class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    def search(self, nums, target):
        def helper(tar):
            # 二分法的下标
            i, j = 0, len(nums) - 1

            while i <= j:
                # 取商
                m = (i + j) // 2
                if nums[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1
            print("return i:", i)
            return i

        return helper(target) - helper(target - 1)


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().search(nums, target))
