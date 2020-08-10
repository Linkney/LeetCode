"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""


# def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
class Solution:
    def combinationSum2(self, candidates, target):
        def dfs(begin, path, residue):
            # 如果残留目标等于0 那么 当前路径已经搞定 全部计入res答案中
            if residue == 0:
                res.append(path[:])
                print('Res path :', path)
                return

            # 遍历 candidates 即 candidates[index] 必取的情况
            for index in range(begin, size):
                # 剩余的最小的都超过了 不用搞了 出去 pop 回溯
                if candidates[index] > residue:
                    break

                # index > begin 第一轮为 False    短路逻辑保证下标不会越界    前一个和后一个 candidate 相等
                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                path.append(candidates[index])
                print('dfs path in:', path, '       startIndex:', index+1, '    resTarget:', residue -candidates[index])
                # 将坐标前移 当前路径和 剩余残差 dfs
                dfs(index + 1, path, residue - candidates[index])
                path.pop()
                print('dfs path pop:', path)

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        print(candidates)
        res = []
        dfs(0, [], target)
        return res


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))
