class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # start, end = 0, 0
        # ans = 0
        #         while end < len(s):
        #             # 在或者不在  不在 end++ ans刷新  在 start++ until 不在
        #             if s[end] not in s[start:end]:
        #                 ans = max(ans, end - start + 1)
        #             else:
        #                 while s[end] in s[start:end]:
        #                     start += 1
        #             end += 1
        #         return ans

        start = 0
        ans = 0
        # char:index
        hashtable = {}

        # 如果一个 字符不在 即 没有出现过 则 加入   如果出现过 则 将 该数重置 并 将 start 刷新

        for end in range(len(s)):
            # 在 刷新 start 不在添加
            if s[end] in hashtable:
                start = max(hashtable[s[end]] + 1, start)
                hashtable[s[end]] = end
            else:
                hashtable[s[end]] = end

            ans = max(ans, end - start + 1)
        return ans


if __name__ == '__main__':
    s = "tmmzuxt"
    print("Ans:", Solution().lengthOfLongestSubstring(s))
