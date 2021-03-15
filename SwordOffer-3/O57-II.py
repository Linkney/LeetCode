"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
"""


# 数学
# target = 求和 x, x+1, x+2, x+3, .....
# 即 target = k * x + b
# 当 上式 成立 即 可 [x, x+1, x+2, ...x+k-1] 成为答案
class Solution:
    # def findContinuousSequence(self, target: int) -> List[List[int]]:
    def findContinuousSequence(self, target):
        # target = k * x + b
        ans = []
        k = 2
        b = 1
        while b < target:
            if (target - b) % k == 0:
                temp = []
                # 构造答案
                x = (target - b) // k
                for i in range(k):
                    temp.append(x+i)
                ans.append(temp)
            b = b + k
            k = k + 1
        ans.reverse()
        # 其实可以优化一下 就先找到 最大的上限 b 然后 倒着来 就不需要 ans.reverse() 了
        return ans

    def findContinuousSequence_MoveWindow(self, target):
        i = 1  # 滑动窗口的左边界
        j = 1  # 滑动窗口的右边界
        sum = 0  # 滑动窗口中数字的和
        res = []
        while i <= target // 2:
            if sum < target:
                # 右边界向右移动
                sum += j
                j += 1
            elif sum > target:
                # 左边界向右移动
                sum -= i
                i += 1
            else:
                # 记录结果
                arr = list(range(i, j))
                res.append(arr)
                # 左边界向右移动
                sum -= i
                i += 1
        return res


if __name__ == '__main__':
    target = 15
    print(Solution().findContinuousSequence(target))

    # print(9 / 2)    # 小数除法
    # print(9 // 2)   # 取商
    # print(9 % 2)    # 取余
