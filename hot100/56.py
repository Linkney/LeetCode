"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间

示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""


# 作者：LeetCode-Solution
# 真特么妙
class Solution2:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


class Solution:
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    def merge(self, intervals):
        ans = []
        for i in range(len(intervals)):
            for j in range(len(ans)):
                # ..
                pass

        return ans

    # 判断两个间隔是否重叠
    def check(self, interval1, interval2):
        start1, end1 = interval1
        start2, end2 = interval2
        if end1 < start2 or end2 < start1:
            return False
        else:
            return True

    # 合并（已知）重叠间隔
    def mergeTwo(self, interval1, interval2):
        start1, end1 = interval1
        start2, end2 = interval2
        start = min(start1, start2)
        end = max(end1, end2)
        return [start, end]


if __name__ == '__main__':
    # intervals = [[1, 4], [4, 5]]
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [2, 3]]
    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    print(Solution2().merge(intervals))
    # interval1 = [1, 4]
    # interval2 = [4, 5]
    # print(Solution().check(interval1, interval2))
    # print(Solution().mergeTwo(interval1, interval2))
