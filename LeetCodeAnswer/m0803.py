"""
魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引
若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。

示例1:
 输入：nums = [0, 2, 3, 4, 5]
 输出：0
 说明: 0下标的元素为0
示例2:
 输入：nums = [1, 1, 1]
 输出：1
说明:
此题为原书中的 Follow-up，即数组中可能包含重复元素的版本
提示:
nums长度在[1, 1000000]之间
"""


# def findMagicIndex(self, nums: List[int]) -> int:
class Solution:
    def findMagicIndex(self, nums):
        # 暴力
        for i in range(len(nums)):
            if i == nums[i]:
                return i
        return -1

    def _findMagicIndex(self, nums):
        # 隔词跳跃 （升序   相当于 两个升序数组 一个是 0 1 2 3 4...  一个是原数组  追及问题）
        for i in range(len(nums)):
            if i == nums[i]:
                return i
            i = max(nums[i], i+1)
            if i >= len(nums):
                break
        return -1
