"""
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 
这里的 left 和 right 代表和 i 相邻的两个气球的序号。
注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
求所能获得硬币的最大数量。

说明:
你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:
输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""


# def maxCoins(self, nums: List[int]) -> int:
class Solution:
    def pprint(self, dp):
        for i in dp:
            print(i)
        print('-------------------------------------')

    def maxCoins(self, nums):
        # dp[i][j] ： 从 i 到 j 个气球（开区间）能够获取的最大的硬币数量  答案即为 0 n-1 即 1 n-2
        # dp[i][j] 即 以某种方式点完 [i+1,j-1] 气球 区间 变 [] 空  返回值为 其最大硬币数
        # dp[i][j] = max{ dp[i][k-1] + dp[k+1][j] + nums[i-1] * nums[k] * nums[j+1] } , i+1<=k<=j-1 ,k 遍历
        #   解释： dp[i][j] 的一种硬币获取方法所得的硬币数  = 最后点爆 nums[k]
        #                  = 不论先后  nums[k]  左边 和 右边的 先全部点完   最后点 nums[k]
        #                  nums[i-1] [i,k-1] nums[k] [k+1,j] nums[j+1]
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        self.pprint(dp)

        for step in range(2, n):
            for i in range(n):
                if step == 2:
                    if i + step < n:
                        dp[i][i + step] = nums[i] * nums[i + 1] * nums[i + 2]
                        self.pprint(dp)
                    continue
                for k in range(i + 1, i + step):
                    if i + step < n:
                        dp[i][i + step] = max(dp[i][k] + dp[k][i + step] + nums[i] * nums[k] * nums[i + step],
                                              dp[i][i + step])
                        self.pprint(dp)

        return dp[0][n-1]


if __name__ == '__main__':
    nums = [3, 1, 5, 8]
    print(Solution().maxCoins(nums))
