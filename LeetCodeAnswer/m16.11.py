"""
你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。
你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。
返回的长度需要从小到大排列。

示例：
输入：
shorter = 1
longer = 2
k = 3
输出： {3,4,5,6}

提示：
0 < shorter <= longer
0 <= k <= 100000
"""


# def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
class Solution:
    def divingBoard(self, shorter, longer, k):
        if k == 0:
            return []
        if shorter == longer:
            return [shorter*k]
        # (0, 1, ..., k) * shorter + (k, k-1, ..., 0) * longer 排序去重
        Ans = []
        for i in range(k+1):
            temp = (k-i) * shorter + i * longer
            Ans.append(temp)
        # Ans.sort()
        return Ans



if __name__ == '__main__':
    shorter = 1
    longer = 2
    k = 3
    s = Solution()
    Ans = s.divingBoard(shorter, longer, k)
    print(Ans)
