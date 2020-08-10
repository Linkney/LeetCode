"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。
"""


# def jump(self, nums: List[int]) -> int:
class Solution:
    def jump(self, nums):
        # 超时了！
        numsLen = len(nums)
        MAXNUM = 999999999999
        # 显然是个动态规划题目 dp[i] 表示到达 i 下标所需要的最少跳跃次数
        # dp[i] = min( dp[x]且x可以跳到i位置 ) 遍历 x
        dp = [MAXNUM for _ in range(numsLen)]
        dp[0] = 0

        for i in range(1, numsLen):
            # print('i:', i)
            for x in range(0, i):
                # print('x:', x, '   nums[x]:', nums[x], '   i:', i)
                if x + nums[x] >= i:
                    # 可以够到
                    dp[i] = min(dp[i], dp[x]+1)
                    # print(dp)

        return dp[-1]

    def _jump(self, nums):
        n = len(nums)
        # 正向贪心
        # 跳step次最远可以跳到end 而如果当前到了end还没到终点说明step次已经不够了 必须要多跳一次才能更远
        # 那么多跳一次能到的最远是哪儿呢 根据计算就是maxPos。
        # 也就是step + 1次最多可以跳到end = maxPos那么远。一直到下一次到end并且没到终点再更新......
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            # print('i:', i, '   maxPos:', maxPos, '  end:', end, '    step:', step)

            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])

                if i == end:
                    end = maxPos
                    step += 1
            print('i:', i, '   maxPos:', maxPos, '  end:', end, '    step:', step)
        return step


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    # nums = [1, 1, 1, 1, 4]
    print(nums)
    print(Solution()._jump(nums))
