# Again 2020年12月9日16:16:28 异或位运算
"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次
请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]

示例 2：
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
"""


# Hash Table
# 位运算
import functools


class Solution:
    # def singleNumbers(self, nums: List[int]) -> List[int]:
    def singleNumbers(self, nums):
        check = {}
        for num in nums:
            if num in check:
                check[num] = check[num] + 1
            else:
                check[num] = 1

        # print(check)
        # print(check.items())
        ans = []
        for item in check.items():
            if item[1] == 1:
                ans.append(item[0])
        # print(ans)
        return ans

    # 异或 位运算
    def singleNumbers2(self, nums):
        ret = functools.reduce(lambda x, y: x ^ y, nums)

        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]


if __name__ == '__main__':
    nums = [4, 1, 4, 6]
    print(Solution().singleNumbers2(nums))
