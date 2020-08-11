"""
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，
并且这些子字符串中的所有0和所有1都是组合在一起的。
重复出现的子串要计算它们出现的次数。

示例 1 :
输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。
另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
示例 2 :
输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        # 状态机    纯0    纯1     01     10   四种状态  '0' '1' '01' '10'
        # 纯0 + 0 = 纯0 （zeroNum++）                 纯0 + 1 = 01      （oneNum++）（ans++）
        # 纯1 + 0 = 10  （oneNum++）（ans++）         纯1 + 1 = 纯1     （oneNum++）
        # 01  + 0 = 10  （zeroNum重置）（ans++）      01  + 1 = 01
        # ...
        state = -1
        zeroNum = 0
        oneNum = 0
        # 初始化 用 s[0]
        if s[0] == '0':
            state = '0'
            zeroNum = 1
        if s[0] == '1':
            state = '1'
            oneNum = 1
        print('State :', state, '    zeroNum: ', zeroNum, '     oneNum: ', oneNum, '     ans:', ans)

        # 算法逻辑
        for i in range(1, len(s)):
            print(s[:i+1])
            print('State :', state, '    zeroNum: ', zeroNum, '     oneNum: ', oneNum, '     ans:', ans)

            if s[i] == '0':
                if state == '0':
                    zeroNum += 1
                    continue
                if state == '1':
                    zeroNum += 1
                    if oneNum >= zeroNum:
                        ans += 1
                    state = '10'
                    continue
                if state == '01':
                    zeroNum = 1
                    if oneNum >= zeroNum:
                        ans += 1
                    state = '10'
                    continue
                if state == '10':
                    zeroNum += 1
                    if oneNum >= zeroNum:
                        ans += 1
                    continue

            if s[i] == '1':
                if state == '0':
                    oneNum += 1
                    if zeroNum >= oneNum:
                        ans += 1
                    state = '01'
                    continue
                if state == '1':
                    oneNum += 1
                    continue
                if state == '01':
                    oneNum += 1
                    if zeroNum >= oneNum:
                        ans += 1
                    continue
                if state == '10':
                    oneNum = 1
                    if zeroNum >= oneNum:
                        ans += 1
                    state = '01'
                    continue

        return ans


if __name__ == '__main__':
    s = "00110011"
    print(Solution().countBinarySubstrings(s))
