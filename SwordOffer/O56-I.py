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
        x, y, n, m = 0, 0, 0, 1     # x y 两个答案  n 遍历异或   m 与运算工具
        for num in nums:  # 1. 遍历异或   n 初始化为 0 不影响 异或运算
            n ^= num
        while n & m == 0:  # 2. 循环左移，计算 m    得到大致这个样子 m = 0000100
            m <<= 1
        for num in nums:  # 3. 遍历 nums 分组
            # 通过 num & m 会将 x 和 y 分到 if else 的两个分支里  其余数分哪无所谓会异或掉自身
            if num & m:
                x ^= num  # 4. 当 num & m != 0
            else:
                y ^= num  # 4. 当 num & m == 0
        return x, y  # 5. 返回出现一次的数字

    # 朴素数组异或
    def xo(self, nums):
        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i]
        return ans


if __name__ == '__main__':
    nums = [4, 1, 4, 6]
    print(Solution().singleNumbers2(nums))

    nums = [1, 2, 2, 1, 4]
    print(Solution().xo(nums))
