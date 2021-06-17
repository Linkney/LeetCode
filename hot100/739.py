"""
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""


class Solution:
    def dailyTemperatures(self, temperatures):
        # 气温列表
        # 要想观测到更高气温的至少等待天数 or 0 表示不会再有更高
        # temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        # 输出应该是     [1,   1,  4,   2,  1,  1,  0, 0]

        # 暴力法   超时
        ans = [0 for _ in range(len(temperatures))]
        for i in range(len(ans)):
            # indexMove = 0
            index = i
            while index < len(temperatures):
                if temperatures[index] > temperatures[i]:
                    break
                index += 1

            if index == len(temperatures):
                ans[i] = 0
            else:
                ans[i] = index - i

        return ans

    def dailyTemperaturesBack(self, temperatures):
        # 倒序填写答案 顺便记下 max 已 快速置 0    还是过不了   还有一个捷径 如果 和 后一个数字一样 则 +1 即可
        ans = [0 for _ in range(len(temperatures))]
        maxB = temperatures[-1]
        for i in range(len(ans)-1, -1, -1):
            print("i:{},   maxB:{}".format(i, maxB))
            if maxB <= temperatures[i]:
                ans[i] = 0
                maxB = temperatures[i]
                continue
            elif temperatures[i] == temperatures[i+1]:
                ans[i] = ans[i+1] + 1
                continue
            else:
                index = i
                while index < len(temperatures):
                    if temperatures[index] > temperatures[i]:
                        break
                    index += 1

                if index == len(temperatures):
                    ans[i] = 0
                else:
                    ans[i] = index - i
        return ans

    # 单调栈解法
    def dailyTemperaturesStack(self, temperatures):
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures((temperatures)))
    print(Solution().dailyTemperaturesBack((temperatures)))
    print(Solution().dailyTemperaturesStack(temperatures))
