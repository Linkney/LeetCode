# Again 2020年12月4日16:14:17  Hard 不想做
"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对
输入一个数组，求出这个数组中的逆序对的总数

示例 1:
输入: [7,5,6,4]
输出: 5
"""


class Solution:
    # 暴力遍历 n^n
    def _reversePairs(self, nums):
        ans = 0
        for i in range(len(nums)):
            pre = nums[i]
            for j in range(i+1, len(nums)):
                if pre > nums[j]:
                    ans += 1
        return ans

    # def reversePairs(self, nums: List[int]) -> int:
    # 归并排序：
    #     所有[逆序对]来源于
    #           左边区间的逆序对；
    #           右边区间的逆序对；
    #           横跨两个区间的逆序对。
    def reversePairs(self, nums):
        # Hard
        pass


if __name__ == '__main__':
    # nums = []
    nums = [7, 5, 6, 4]
    print(Solution().reversePairs(nums))
