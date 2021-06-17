'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c
使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组

注意：答案中不可以包含重复的三元组。
'''
# class Solution:
#     def threeSum(self, nums):
#         # a + b + c = 0
#         n = len(nums)
#
#         if n < 3:
#             return []
#
#         nums.sort()  # 从小到大排序
#         res = []
#
#         for i in range(n):
#             # 遍历 左元素  左元素大于 0 即可以结束了 return 当前存的答案
#             if nums[i] > 0:
#                 return res
#             if i > 0 and nums[i] == nums[i - 1]:
#                 # 和上一次的元素 重复
#                 continue
#
#             L = i + 1  # 中元素
#             R = n - 1  # 右元素
#             while L < R:  # 还没撞到 还有机会
#                 if nums[i] + nums[L] + nums[R] == 0:
#                     res.append([nums[i], nums[L], nums[R]])
#                     # 成功后的后处理
#                     while L < R and nums[L] == nums[L + 1]:
#                         L = L + 1
#                     while L < R and nums[R] == nums[R - 1]:
#                         R = R - 1
#                     # 前进 寻找 新的配对
#                     L = L + 1
#                     R = R - 1
#                 elif nums[i] + nums[L] + nums[R] > 0:
#                     R = R - 1
#                 else:
#                     L = L + 1
#         return res


def threeSum(nums):
    if len(nums) < 3:
        return []

    # a + b + c = 0
    ans = []

    nums.sort()
    print("nums after sort:", nums)

    for a in range(len(nums)):
        # a 已经跑完 即 结束
        if nums[a] > 0:
            return ans
        # 重复元素 第一个index = 0 不判断 短路
        if a > 0 and nums[a] == nums[a - 1]:
            continue

        b = a + 1
        c = len(nums) - 1
        while b < c:
            print("Checking index a={}, b={}, c={}".format(a, b, c))
            if nums[a] + nums[b] + nums[c] == 0:
                ans.append([nums[a], nums[b], nums[c]])
                # 成功后的处理 跨越重复元素
                while b < c and nums[b] == nums[b + 1]:
                    b += 1
                while b < c and nums[c] == nums[c - 1]:
                    c -= 1
                b += 1
                c -= 1
            # 不成功
            else:
                if nums[a] + nums[b] + nums[c] > 0:
                    c -= 1
                else:
                    b += 1
    return ans


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    print(threeSum(nums))