"""
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]
其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]   即 除 i 下标以外的其它所有数的乘积
不能使用除法

示例:
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
"""


class Solution:
    # def constructArr(self, a: List[int]) -> List[int]:
    # 暴力法超时
    #       显而易见的重复运算
    def constructArr(self, a):
        ans = [1 for _ in range(len(a))]

        for ansi in range(len(ans)):
            for prev in range(0, ansi):
                ans[ansi] *= a[prev]
            for later in range(ansi+1, len(a)):
                ans[ansi] *= a[later]

        return ans

    # 结果集中任何一个元素 = 其左边所有元素的乘积 * 其右边所有元素的乘积。
    # 一轮循环构建左边的乘积并保存在结果集中
    # 二轮循环 构建右边乘积的过程，乘以左边的乘积，并将最终结果保存
    def constructArr2(self, a):
        ans = [1] * len(a)
        for i in range(1, len(a)):
            # 把左边的先都乘上了   从左到右
            ans[i] = ans[i-1] * a[i-1]

        temp = 1
        for i in range(len(a)-2, -1, -1):
            # 在乘右侧的 从右到左
            temp *= a[i+1]
            ans[i] *= temp
        return ans


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(Solution().constructArr(a))
    print(Solution().constructArr2(a))
