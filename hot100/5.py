# def expendmid(self, s, l, r):
#     while (l >= 0 and r < len(s) and s[l] == s[r]):
#         l = l - 1
#         r = r + 1
#     return r - l + 1 - 2
#
#
# def longestPalindrome(self, s: str) -> str:
#     start = 0
#     end = 0
#     for i in range(len(s)):
#         len1 = self.expendmid(s, i, i)
#         len2 = self.expendmid(s, i, i + 1)
#         lenmax = max(len1, len2)
#         if lenmax > (end - start + 1):
#             if len1 > len2:
#                 # 奇
#                 end = int(i + (lenmax - 1) / 2)
#                 start = int(i - (lenmax - 1) / 2)
#             else:
#                 end = int(i + lenmax / 2)
#                 start = int(i - lenmax / 2 + 1)
#     return s[start: end + 1]


class Solution:
    # 输入 l r index 向两边延伸知道 最大回文 返回 最大回文 和 其 length
    def expendCenter(self, left, right, s):
        tempLength = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            tempLength = max(tempLength, right - left + 1)
            left -= 1
            right += 1
        return tempLength, s[left + 1: right + 1 - 1]

    def longestPalindrome(self, s: str) -> str:
        ans = ""
        maxLength = 0

        for i in range(len(s)):
            tempLength, tempAns = self.expendCenter(i, i, s)
            if tempLength > maxLength:
                maxLength = tempLength
                ans = tempAns
            tempLength, tempAns = self.expendCenter(i, i + 1, s)
            if tempLength > maxLength:
                maxLength = tempLength
                ans = tempAns
        return ans


if __name__ == '__main__':
    s = "a"
    ans = Solution().longestPalindrome(s)
    print(ans)

