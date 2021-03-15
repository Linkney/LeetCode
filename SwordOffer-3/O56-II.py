"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次
请找出那个只出现一次的数字

示例 1：
输入：nums = [3,4,3,3]
输出：4

示例 2：
输入：nums = [9,1,7,9,7,9,7]
输出：1
"""


# 从二进制角度看
# 统计所有数字的各二进制位中 1 的出现次数，并对 3 求余，结果则为只出现一次的数字
class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    # 我选择原地裂开    有限状态自动机
    def singleNumber(self, nums):
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones

    # 遍历统计
    def singleNumber2(self, nums):
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)


if __name__ == '__main__':
    nums = [9, 1, 7, 9, 7, 9, 7]
    print(Solution().singleNumber(nums))
