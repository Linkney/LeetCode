# Again 2020年11月23日15:22:17 全排列 dfs
"""
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
"""


class Solution:
    # def permutation(self, s: str) -> List[str]:
    def permutation(self, s):
        c = list(s)
        # print("c:", c)
        ans = []

        def dfs(x):
            if x == len(c) - 1:
                # 添加排列方案
                ans.append(''.join(c))
                return
            dic = set()
            for i in range(x, len(c)):
                # 重复，因此剪枝
                if c[i] in dic:
                    continue
                dic.add(c[i])
                # 交换，将 c[i] 固定在第 x 位
                c[i], c[x] = c[x], c[i]
                # 开启固定第 x + 1 位字符
                dfs(x + 1)
                # 恢复交换
                c[i], c[x] = c[x], c[i]

        dfs(0)
        return ans


if __name__ == '__main__':
    s = "abc"
    print(Solution().permutation(s))
