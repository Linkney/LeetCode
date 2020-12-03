"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""
from collections import deque


# 队列结构
#       队列中没有重复元素 则入队
#       有重复元素 则出队至 将重复元素出去
#           刷新整个过程中的 max Queue Length
#               Ps: 这不就是 滑动窗口 双指针即可解决（双指针数组切片判断 in）
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxQueueLength = 0
        queue = deque()
        # print(queue)
        for i in range(len(s)):
            if s[i] not in queue:
                queue.append(s[i])
            else:
                while s[i] in queue:
                    queue.popleft()
                queue.append(s[i])
            # print(queue)
            maxQueueLength = max(maxQueueLength, len(queue))

        return maxQueueLength


if __name__ == '__main__':
    # s = "abcabcbb"
    s = "bbbbb"
    # s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))
