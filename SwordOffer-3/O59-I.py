"""
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值

示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]

解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

提示：
你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
"""
import collections


class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # 暴力
    def maxSlidingWindow(self, nums, k):
        if len(nums) == 0:
            return []
        ans = []
        for i in range(len(nums)-k+1):
            ans.append(max(nums[i:i+k]))
        return ans

    # Queue辅助
    def maxSlidingWindow2(self, nums, k):
        # 特殊情况
        if not nums or k == 0:
            return []

        # 大 - 中 - 小     大 为当前窗口 max
        deque = collections.deque()
        # 未形成窗口
        for i in range(k):
            # 队列 有东西 而且 队列最后一个 更小  刷新 max
            while deque and deque[-1] < nums[i]:
                deque.pop()

            deque.append(nums[i])
        # 首个窗口答案出现
        res = [deque[0]]

        # 形成窗口后
        for i in range(k, len(nums)):
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])

            res.append(deque[0])
        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))
