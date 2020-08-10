"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


# def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
class Solution:
    def groupAnagrams(self, strs):
        # 字母：个数 一致即可视为一类
        dic = {}
        for s in strs:
            keys = "".join(sorted(s))
            print(keys)
            if keys not in dic:
                dic[keys] = [s]
            else:
                dic[keys].append(s)
        print(dic)
        return list(dic.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))

    # 字符串 sorted
    # s1 = "eat"
    # s2 = "tae"
    # s1 = sorted(s1)
    # s2 = sorted(s2)
    # print(s1, s2)
