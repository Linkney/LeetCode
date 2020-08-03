"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:
输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:
输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:
输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:
输入:
s = "acdcb"
p = "a*c?b"
输出: false
"""


class Solution:
    def pprint(self, dp):
        for i in dp:
            print(i)
        print('-------------------------------')

    def isMatch(self, s: str, p: str) -> bool:
        # ? 一个字符  * 任意
        lenS, lenP = len(s), len(p)

        # dp[i][j] 表示字符串 s 的前 i 个字符和模式 p 的前 j 个字符是否能匹配
        dp = [[False] * (lenP + 1) for _ in range(lenS + 1)]
        self.pprint(dp)
        # 初始值 双 空 能互相匹配
        dp[0][0] = True

        # 字符串长度不涨  模式长度涨  在 s 为 空的情况下 p 必须 * 打头 且 全为 * 才是 True
        for i in range(1, lenP + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        self.pprint(dp)
        # 第一行初始化值完毕 即 s = ''  的情况下  s 和 p[切片] 的匹配情况

        for i in range(1, lenS + 1):
            for j in range(1, lenP + 1):
                # 一行一行算  i 是 s ， j 是 p （字符串多一个 p 遍历）
                # 差值匹配 左边和上边  p 为一个 *  p 可以白涨 即 * 匹配 空  dp[i][j-1]
                # 也可以使用这个 *  状态则由 dp[i-1][j] 而来 即 * 匹配 s[i]
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                # 单个匹配 左上角 s +1 p +1 关系递推
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                self.pprint(dp)
        return dp[lenS][lenP]


if __name__ == '__main__':
    s = 'zxc'
    p = 'z*?'
    print(Solution().isMatch(s, p))
