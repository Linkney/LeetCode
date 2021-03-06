"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。
示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
from typing import List


class Solution:
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    def permuteUnique(self, nums):
        # dfs 框架
        # [1, 1, 2] , 3 , 0 , [] , [False, False, False] , []
        def dfs(nums, size, depth, path, used, res):
            # 深度 和 size 一样  （深度 即 ）
            if depth == size:
                res.append(path.copy())
                return

            for i in range(size):
                if not used[i]:

                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        print('size:', size)
        if size == 0:
            return []

        nums.sort()
        print('nums:', nums)

        used = [False] * len(nums)
        print('used:', used)

        res = []
        print('res:', res)

        dfs(nums, size, 0, [], used, res)

        return res


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))
