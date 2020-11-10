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

        maxNum = 0
        power = 0
        while n != 0:
            n = n - 1
            maxNum += 9 * 10 ** power
            power += 1
        # print("maxNum:", maxNum)
        ans = [i for i in range(1, maxNum+1)]
        return ans


if __name__ == '__main__':
    print(Solution().printNumbers(2))
