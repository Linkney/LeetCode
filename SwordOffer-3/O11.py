"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：
输入：[3,4,5,1,2]
输出：1
示例 2：
输入：[2,2,2,0,1]
输出：0
"""


class Solution:
    # def minArray(self, numbers: List[int]) -> int:
    # 寻找逆序对
    def minArray(self, numbers):
        for index in range(len(numbers)-1):
            if numbers[index] > numbers[index+1]:
                return numbers[index+1]
        # 0个元素被旋转
        return numbers[0]

    # 二分法      大 min 小  升序
    def minArray2(self, numbers):
        left, right = 0, len(numbers) - 1
        while left < right:
            print(left, right)
            # mid = (left + right) // 2
            mid = left + (right - left) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                return min(numbers[left:right])
        return numbers[left]


if __name__ == '__main__':
    # numbers = [3, 4, 5, 1, 2]
    numbers = [1, 3, 5, 6, 8]
    print(Solution().minArray(numbers))
    print(Solution().minArray2(numbers))
    print(Solution().minArray3(numbers))
