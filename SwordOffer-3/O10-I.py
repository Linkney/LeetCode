"""
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：n = 2
输出：1
示例 2：
输入：n = 5
输出：5
"""


# 递归
# 递推
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        ans = [-1 for _ in range(n+1)]
        ans[0] = 0
        ans[1] = 1
        for index in range(2, n+1):
            ans[index] = ans[index-1] + ans[index-2]
        return ans[n] % 1000000007

    def fib2(self, n: int) -> int:
        if n <= 1:
            return n
        fn0 = 0
        fn1 = 1
        # 进一次小循环 fn1 为 fn2
        for _ in range(n-1):
            sum = fn0 + fn1
            fn0 = fn1
            fn1 = sum % 1000000007
        return fn1


if __name__ == '__main__':
    n = 5
    print(Solution().fib(n))
    print(Solution().fib2(n))
