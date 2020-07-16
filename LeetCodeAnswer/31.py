"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


# def nextPermutation(self, nums: List[int]) -> None:
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. 将数变大  即  将 低位 的  大数  和  高位的  小数 交换   （数字变大）
        # 2. 将 尽可能  小的 "大数"   去 和  尽可能 低的  "高位"   去交换   （下一个排列）
        # 3. 交换后 将 尾部 置为 升序  （最小）



        for i in range(len(nums)-2, -1, -1):
            # 从倒数第二个数开始 遍历到 第一个数  找 逆序
            print('nums[i]:', nums[i], " i :", i)
            if nums[i+1] > nums[i]:
                # nums[i] 为 高位 大数
                for j in range(i+1, len(nums), 1):
                    print("j :", j)
                    # 从 i 后面一个数开始遍历 直到找到 最小 大于他的数     [短路逻辑 如果超下标了 就直接短路]
                    if ((j+1) == len(nums)) or ( nums[i] < nums[j] and nums[i] >= nums[j+1] ):
                        # 逻辑补丁  丑陋
                        if nums[j] <= nums[i]:
                            j = j - 1
                        # nums[j] 即要和 nums[i] 交换
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
                        print("nums:", nums, " i :", i)
                        # 尾部升序排列  i+1 到最后   涉及到 列表 部分 排序 [:].sort 切片排序无效
                        nums_part_sorted = sorted(nums[i+1:])
                        nums[i+1:] = nums_part_sorted
                        return
        print("没有逆序")
        nums.sort()
        return


if __name__ == '__main__':
    # nums = [1, 2, 3]
    # nums = [3, 2, 1]
    # nums = [1, 3, 2]
    # nums = [1, 5, 1]
    nums = [2, 2, 7, 5, 4, 3, 2, 2, 1]
    Solution().nextPermutation(nums)
    print(nums)

