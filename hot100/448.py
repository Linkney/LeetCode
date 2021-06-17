"""
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        #  1 2 3 4 5
        # [1 2 3 4 5]
        # [1 2 2 4 4]

        # [4,3,2,7,8,2,3,1]
        # [1 2 2 3 3 4 7 8]
        # [1 2 3 4 5 6 7 8]

        # 将所有正数作为数组下标，置对应数组值为负值。那么，仍为正数的位置即为（未出现过）消失的数字。
        # 这
        ans = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
            # print(nums)

        # print("After :   ", nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(nums))
