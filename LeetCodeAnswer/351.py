"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]

示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

进阶:
如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""


# def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
class Solution:
    def intersect(self, nums1, nums2):
        ans = []
        # 1. 暴力 O(n^2)   相同 nums1&nums2 . remove       ans . append
        # 2. 排序 O(nlogn) 双指针 O(n+m)   nums1&nums2 . remove       ans . append

        # 3. Hash Table

        print(nums1)
        print(nums2)
        index1 = 0
        index2 = 0
        nums1.sort()
        nums2.sort()
        print(nums1)
        print(nums2)
        # 只要两个指针下标还没越界 还得到最后
        while index1 <= (len(nums1)-1) and index2 <= (len(nums2)-1):
            if nums1[index1] == nums2[index2]:
                ans.append(nums1[index1])
                index1 = index1 + 1
                index2 = index2 + 1
                continue
            if nums1[index1] < nums2[index2]:
                index1 = index1 + 1
                continue
            if nums1[index1] > nums2[index2]:
                index2 = index2 + 1
                continue

        return ans


if __name__ == '__main__':
    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    s = Solution()
    ans = s.intersect(nums1, nums2)
    print("Ans is :", ans)
