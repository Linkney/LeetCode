"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:
s = "abaccdeff"
返回 "b"

s = ""
返回 " "
"""
from collections import deque


# 一次遍历 队列保留
#       如果 不在队列中 则 添加
#       如果 在队列中   则 添加到 cut
class Solution:
    def firstUniqChar(self, s: str) -> str:
        queue = deque()
        cut = set()
        for i in range(len(s)):
            if s[i] not in queue:
                queue.append(s[i])
            else:
                if s[i] not in cut:
                    cut.add(s[i])
        for item in cut:
            queue.remove(item)
        if len(queue) == 0:
            return " "
        return queue.popleft()


if __name__ == '__main__':
    # s = "abaccdeff"
    s = "aadadaad"
    print(Solution().firstUniqChar(s))
