"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
"""


# 双指针碾压墙
class Solution:
    # def exchange(self, nums: List[int]) -> List[int]:
    def exchange(self, nums):
        if len(nums) == 0:
            return nums
        indexJi = 0
        indexOu = len(nums) - 1
        i = 0
        while indexJi != indexOu:
            print("i:", i, "    indexJi:", indexJi, "    indexOu:", indexOu)
            print(nums)
            if nums[i] % 2 == 1:
                temp = nums[indexJi]
                nums[indexJi] = nums[i]
                nums[i] = temp
                indexJi += 1
            else:
                temp = nums[indexOu]
                nums[indexOu] = nums[i]
                nums[i] = temp
                indexOu -= 1
            i += 1
            if i >= indexOu:
                i = indexJi
        return nums


if __name__ == '__main__':
    nums = [2,16,3,5,13,1,16,1,12,18,11,8,11,11,5,1]
    print(Solution().exchange(nums))
