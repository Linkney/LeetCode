# Again 2020年11月28日11:08:33 dp
"""
给定一个数字，我们按照如下规则把它翻译为字符串：
0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。


示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
"""


# 0 1 2 3 4 5 6 7 8 9     10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# a b c d e f g h i j     k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
# dp 动态规划 （没看出来么）  f(i) = 第 i 位结尾的前缀串翻译的方案数
#       f(i) = f(i-1) + f(i-2) ,[i-1 > 0 且    10 < i-1,i 形成的数字 < 25 ]
#           f(-1) = 0  f(0) = 1
class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1
        if (num % 100 < 26) and (num % 100 > 9):
            # f(i) = f(i-1) + f(i-2) ,[i-1 > 0 且    10 < i-1,i 形成的数字 < 25 ]
            return self.translateNum(num // 10) + self.translateNum(num // 100)
        else:
            # f(i) = f(i-1)
            return self.translateNum(num // 10)

    # 正向动态规划  f(i) = f(i-1) + f(i-2)
    def translateNumDP(self, num):
        # 实现起来有点遭重 需要数据类型的转换
        ans = [-1 for _ in range(len(str(num)))]
        print(ans)
        # todo .....


if __name__ == '__main__':
    num = 12258
    print(Solution().translateNum(num))
    print(Solution().translateNumDP(num))
