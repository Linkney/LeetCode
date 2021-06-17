"""
给你一个整数数组 nums ，数组中的元素 互不相同        返回该数组所有可能的子集（幂集）
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]
"""


class Solution(object):
    # 回溯
    def subsets(self, nums):
        res = [[]]
        for i in range(len(nums) - 1, -1, -1):
            for subres in res[:]:
                res.append(subres + [nums[i]])
        return res

    # 迭代
    def subsets2(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
    print(Solution().subsets2(nums))
