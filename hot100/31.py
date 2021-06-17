"""
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。

示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]

示例 4：
输入：nums = [1]
输出：[1]
"""
class Solution:
    # def nextPermutation(self, nums: List[int]) -> None:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. 将数变大  即  将 低位 的  大数  和  高位的  小数 交换   （数字变大）
        # 2. 将 尽可能  小的 "大数"   去 和  尽可能 低的  "高位"   去交换   （下一个排列）
        # 3. 交换后 将 尾部 置为 升序  （最小）



        for i in range(len(nums)-2, -1, -1):
            # 从倒数第二个数开始 遍历到 第一个数  找 逆序
            if nums[i+1] > nums[i]:
                # nums[i] 为 高位 大数
                for j in range(i+1, len(nums), 1):
                    # 从 i 后面一个数开始遍历 直到找到 最小 大于他的数     [短路逻辑 如果超下标了 就直接短路]
                    if ((j+1)==len(nums)) or (nums[i] < nums[j] and nums[i] >= nums[j+1]):
                        # nums[j] 即要和 nums[i] 交换
                        if nums[j] <= nums[i]:
                            j = j - 1
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
                        # 尾部升序排列  i+1 到最后
                        nums_part_sorted = sorted(nums[i+1:])
                        nums[i+1:] = nums_part_sorted
                        return
        nums.sort()
        return


# func nextPermutation(nums []int) {
# 	if len(nums) <= 1 {
# 		return
# 	}
#
# 	i, j, k := len(nums)-2, len(nums)-1, len(nums)-1
#
# 	// find: A[i]<A[j]
# 	for i >= 0 && nums[i] >= nums[j] {
# 		i--
# 		j--
# 	}
#
# 	if i >= 0 { // 不是最后一个排列
# 		// find: A[i]<A[k]
# 		for nums[i] >= nums[k] {
# 			k--
# 		}
# 		// swap A[i], A[k]
# 		nums[i], nums[k] = nums[k], nums[i]
# 	}
#
# 	// reverse A[j:end]
# 	for i, j := j, len(nums)-1; i < j; i, j = i+1, j-1 {
# 		nums[i], nums[j] = nums[j], nums[i]
# 	}
# }


# def nextPermutation(self, nums: List[int]) -> None:
def nextPermutation(self, nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # 1. 将数变大  即  将 低位 的  大数  和  高位的  小数 交换   （数字变大）
    # 2. 将 尽可能  小的 "大数"   去 和  尽可能 低的  "高位"   去交换   （下一个排列）
    # 3. 交换后 将 尾部 置为 升序  （最小）

    if len(nums) <= 1:
        return nums

    # index of nums [    .....    i, jk]
    i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1

    # find  nums[i] < nums[j]
    while i >= 0 and nums[i] >= nums[j]:
        i -= 1
        j -= 1

    # i 需要替换的高位的 小数 在 i+1: -1 中寻找 比 它大一丢丢的数 交换
    # 判断是否到头了还没 到头了会变 -1
    if i >= 0:
        while nums[i] >= nums[k]:
            k -= 1

        nums[i], nums[k] = nums[k], nums[i]

    # index i+1 到 -1  必然为降序
    for k in range((len(nums) - i) // 2):
        nums[i + k], nums[len(nums) - 1 - k] = nums[len(nums) - 1 - k], nums[i + k]



























