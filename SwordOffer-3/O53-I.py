"""
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
"""


# 二分法
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
                # 问：这里为什么是 小于等于？  答：因为题目适当变化 helper（target） - helper（target）
                if nums[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1

                print("i:", i, " j:", j)
            print("return i:", i)
            return i

        return helper(target) - helper(target - 1)


# 常规二分法
def BinarySearch(array, target):
    low = 0
    height = len(array) - 1
    while low < height:
        mid = (low + height) // 2
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            height = mid - 1
        else:
            return array[mid]
    return -1


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().search(nums, target))
    nums = [1, 2, 3, 4, 5, 6]
    target = 7
    print("Target from BinarySearch:", BinarySearch(nums, target))
