"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]

说明：
用返回一个整数列表来代替打印
n 为正整数
"""


class Solution:
    # def printNumbers(self, n: int) -> List[int]:
    def printNumbers(self, n):
        if n < 1:
            return None
        maxNum = 10 ** n - 1
        # print("maxNum:", maxNum)
        ans = [i for i in range(1, maxNum+1)]
        return ans

    # 考虑大数打印问题
    def printNumbers2(self, n):
        def dfs(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0': res.append(int(s))
                if n - self.start == self.nine: self.start -= 1
                return
            for i in range(10):
                if i == 9: self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1

        num, res = ['0'] * n, []
        self.nine = 0
        self.start = n - 1
        dfs(0)
        return res


if __name__ == '__main__':
    print(Solution().printNumbers(2))
    print(Solution()._printNumbers(2))
