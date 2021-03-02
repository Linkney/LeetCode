# Again 2020年11月9日16:27:50 动态规划 或 递归
"""
请实现一个函数用来匹配包含'. '和'*'的正则表达式。
模式中的字符'.'表示任意一个字符          而'*'表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:
输入:
s = "aa"
p = "a"
输出: false

示例 2:
输入: s = "aa"  p = "a*"
输出: true

示例 3:
输入: s = "ab"  p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:
输入: s = "aab"  p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入: s = "mississippi"  p = "mis*is*p*."
输出: false

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。
"""


# dp [i][j] 字符串前i 模式串前j 能否匹配
# 已知 dp[0][0] = True      dp[1,2,3...][0] = False
#
#       T   ?   ?   ....    ?
#       F   ?   ?   ....    ?
#       .
#       .
#       F                   ? = Ans
#       已知  已知
#       已知  未知
# 字符 + 字母  模式 + 字母
#              模式 + 点
#              模式 + 星
# 情况字母和.对上：
#     字母对字母或者. 对上了
# 情况*：
#     * 前一个没对上
#     * 前一个对上了
#           * 作 0
#           * 作 1
#           * 作 多
# 情况其他：
#     失败
class Solution:
    def showdp(self, dp):
        for i in dp:
            print(i)
        print('---------------------')

    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        self.showdp(dp)
        # 初始化初值   空空
        dp[0][0] = True
        self.showdp(dp)
        # 特殊情况 字符串 空  模式串 小概率 a*b*.. 能够 形成 True（间隔形成）   （偶数 且 135..位置为* 且有前继性）
        for j in range(1, len(dp[0])):
            if j >= 2 and p[j-1] == "*" and j % 2 == 0 and dp[0][j-2] is True:
                dp[0][j] = True
        self.showdp(dp)
        #      T___
        # 动归 | ??
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                # 字符串 下标 i-1 位置  模式串 下标 j-1 位置
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                # 模式串 从第二位开始 且 为 星 *            情况：  字符：已知a   模式：已知*
                elif p[j-1] == "*" and j >= 2:
                    # 模式串的 前一位没对上 * 可以置 0 弥补错误
                    if p[j-2] != s[i-1] and p[j-2] != ".":
                        dp[i][j] = dp[i][j-2]
                    # 前一位对上了！ * 让前面的不出现[j-2]   让前面的只出现一次 [j-1]    ！  让前面的出现多次 [i-1]
                    else:
                        dp[i][j] = dp[i][j-2] or dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False
        self.showdp(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    # s = "mississippi"
    # p = "mis*is*p*."
    s = "aab"
    p = "c*a*b"
    print(Solution().isMatch(s, p))
