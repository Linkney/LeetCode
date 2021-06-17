"""
回溯问题

1.有效结果
    仍然是当前结果的长度==列表的长度，即为找到了一个有效结果

2.回溯范围及答案更新
    仍然是全部遍历，因为每一层都要考虑全部元素
    答案更新仍然是在修改 check 之后回溯内部累加更新 sol

3.剪枝条件
    在之前的 剪枝条件1：用过的元素不能再使用之外，又添加了一个新的剪枝条件，
    也就是我们考虑重复部分思考的结果，于是 剪枝条件2：当当前元素和前一个元素值相同（此处隐含这个元素的 index>0 ）
    并且前一个元素还没有被使用过的时候，我们要剪枝

"""
# 无重复元素的全排列
class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    def permute(self, nums):
        # return list(itertools.permutations(nums))
        res = []

        # 参数倒入
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return

            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


# 重复元素的全排列
class Solution2:
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    def permuteUnique(self, nums):
        nums.sort()
        res = []

        def back(nums, temp):
            if not nums:
                res.append(temp)
                return
            else:
                for i in range(len(nums)):
                    # 这种拼接方法是天然的标记，判断前一字符是否在循环里
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    back(nums[:i] + nums[i+1:], temp + [nums[i]])

        back(nums, [])
        return res


if __name__ == '__main__':
    nums = [1, 2, 2]
    print(Solution().permute(nums))
    print(Solution2().permuteUnique(nums))
