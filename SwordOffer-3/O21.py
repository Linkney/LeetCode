"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一
"""


class Solution:
    # def exchange(self, nums: List[int]) -> List[int]:
    # 双指针碾压墙
    def exchange(self, nums):
        if len(nums) == 0:
            return nums
        indexJi = 0
        indexOu = len(nums) - 1
        i = 0
        while indexJi != indexOu:
            # print("i:", i, "    indexJi:", indexJi, "    indexOu:", indexOu)
            # print(nums)
            # 判断奇偶 通过 temp 放入对应侧 对应侧碾压墙 前进
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
            # i 跑的快 = J Q 碾压的量       J O  中间的内容为 待处理的内容
            if i >= indexOu:
                i = indexJi
        return nums

    # 首尾指针  左边的遇到奇数就跳过   右边的遇到偶数就跳过   遇到另一个就停止等待 等两个都停止则交换
    def exchange2(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            while left < right and nums[left] & 1 == 1:
                left += 1
            # left 进入停止等待
            while left < right and nums[right] & 1 == 0:
                right -= 1
            # right 进入停止等待
            nums[left], nums[right] = nums[right], nums[left]

        return nums


if __name__ == '__main__':
    nums = [2,16,3,5,13,1,16,1,12,18,11,8,11,11,5,1]
    # print(Solution().exchange(nums))
    print(Solution().exchange2(nums))
