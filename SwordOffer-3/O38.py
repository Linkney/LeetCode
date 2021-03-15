# <Todo 2021年3月3日20:18:55>
# Again 2020年11月23日15:22:17 全排列 dfs
"""
输入一个字符串，打印出该字符串中字符的所有排列
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
"""


class Solution:
    # def permutation(self, s: str) -> List[str]:
    # 看不懂 2020年12月17日15:35:03
    # 晚上头晕看不进去 2021年3月3日19:47:40
    def permutation(self, s):
        c = list(s)     # ['a', 'b', 'c']  分词放入 list
        print("c:", c)
        ans = []

        def dfs(x):
            # 最后一个玩意了
            if x == len(c) - 1:
                # 添加排列方案
                ans.append(''.join(c))
                return

            # 重复处理装置
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
    s = "abcc"
    print(Solution().permutation(s))

    ans = ['1', '2']
    ans.append(''.join(['a', 'b']))
    print(ans)
