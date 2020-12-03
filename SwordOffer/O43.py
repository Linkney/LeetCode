# Again 2020年11月25日20:06:15 太难了感觉不用 Again 了
"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

示例 1：
输入：n = 12
输出：5

示例 2：
输入：n = 13
输出：6
"""


# ???
# 蛮力  超出时间限制
# class Solution:
#     def countDigitOne(self, n: int) -> int:
#         def checkOne(num):
#             num = str(num)
#             ans = 0
#             for index in range(len(num)):
#                 if num[index] == "1":
#                     ans += 1
#             return ans
#
#         ans = 0
#         for i in range(n+1):
#             ans += checkOne(i)
#         return ans


# 究极黑暗： 还没看过
#       密码锁
class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res


if __name__ == '__main__':
    print(Solution().countDigitOne(98))
