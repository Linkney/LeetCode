"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数
说明:  

1 是丑数。
n 不超过1690。
"""


# 丑数的生长
#       丑数的传递性  即  丑数 * 2 * 3 * 5 还是丑数
#       [1]
#       Math
#       [1, 2, 3, 4, 5, 6, 8] 已知丑数序列 求 下一个丑数 = a*2 or b*3 or c*5
#           且 a b c 三者各自有位序性
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1 for _ in range(n)]
        # 三指针 生长
        a, b, c = 0, 0, 0

        # 生长ing
        for i in range(1, n):
            n2 = ans[a] * 2
            n3 = ans[b] * 3
            n5 = ans[c] * 5
            ans[i] = min(n2, n3, n5)
            if ans[i] == n2:
                a += 1
            if ans[i] == n3:
                b += 1
            if ans[i] == n5:
                c += 1
        return ans[-1]


if __name__ == '__main__':
    n = 10
    print(Solution().nthUglyNumber(n))
