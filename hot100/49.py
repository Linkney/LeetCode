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


class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(self, strs):
        # Idea 质数表示26个字母，把字符串的各个字母相乘   这样可保证字母异位词的乘积必定是相等的

        # 字母：个数 一致即可视为一类
        # 对字符串进行排序   ↑ 会被排序为同一个字符串
        dic = {}
        for s in strs:
            keys = "".join(sorted(s))

            if keys not in dic:
                dic[keys] = [s]
            else:
                dic[keys].append(s)

        return list(dic.values())


if __name__ == '__main__':
    s = "ear"
    s = sorted(s)
    print(s)

    dic = {}
    dic["ab"] = [12]
    dic["ab"].append(21)
    dic["bc"] = [33]
    print(dic)
    print(dic.values())

