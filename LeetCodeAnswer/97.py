"""
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
"""


class Solution:
    def pprint (self, f):
        for i in range(len(f)):
            print(f[i])
        print('-----------------------------------------')

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != (len(s1) + len(s2)):
            return False
        # 动态规划 f(i, j) 表示 s1的前 i 部分  和 s2 的 前 j 部分 能够交错表示 s3 的 前 i+j 部分
        # f(i,j) = { f(i−1,j)and s1[i-1]==s3[i+j-1] } or { f(i, j-1) and s2[j-1] == s3[i+j-1] }
        # 左 和 上 推得   左 上 扩容一圈   答案 即为 右下角格子

        f = [[False for _ in range(len(s2)+2)] for __ in range(len(s1)+2)]
        # f[1][1] = True
        self.pprint(f)

        for row in range(1, len(s1)+2, 1):
            for col in range(1, len(s2)+2, 1):
                if row == 1 and col == 1:
                    f[row][col] = True
                    continue

                f[row][col] = (f[row-1][col] and s1[row-2] == s3[row+col-3]) \
                              or (f[row][col-1] and s2[col-2] == s3[row+col-3])

                self.pprint(f)

        return f[-1][-1]


if __name__ == '__main__':
    s1 = 'abc'
    s2 = 'abcd'
    s3 = 'abcabcd'
    print(Solution().isInterleave(s1, s2, s3))

