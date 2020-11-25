"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 """


# 极端情况 [ 1 1 1 2 3 ]  [ 1 2 3 3 3 ]  [ 1 1 1 2 ]
class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    def majorityElement(self, nums):
        nums.sort()
        return nums[int(len(nums)/2)]


if __name__ == '__main__':
    print(int(5 / 2))
    print(int(4 / 2))
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(Solution().majorityElement(nums))

# 最佳解法：
#       摩尔投票法
#       核心就是对拼消耗
# 玩一个诸侯争霸的游戏，假设你方人口超过总人口一半以上，并且能保证每个人口出去干仗都能一对一同归于尽
# 最后还有人活下来的国家就是胜利。那就大混战呗，最差所有人都联合起来对付你（对应你每次选择作为计数器的数都是众数）
# 或者其他国家也会相互攻击（会选择其他数作为计数器的数），但是只要你们不要内斗，最后肯定你赢。最后能剩下的必定是自己人

# votes, count = 0, 0
# for num in nums:
#     if votes == 0:
#       x = num
#     if num == x:
#       votes += 1
#     else:
#       votes -= 1
