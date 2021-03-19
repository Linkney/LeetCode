# todo 2021年3月3日20:41:17
"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]
"""
import heapq
import random


class Solution:
    # def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
    def getLeastNumbers(self, arr, k):
        arr.sort()
        # 还得去重
        arrNoSame = []
        for i in arr:
            if i not in arrNoSame:
                arrNoSame.append(i)
        return arrNoSame[0:k]

    # 堆 todo>
    def getLeastNumbers2(self, arr, k):
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans


# 快速选择 todo>
class Solution:
    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def randomized_partition(self, nums, l, r):
        i = random.randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return self.partition(nums, l, r)

    def randomized_selected(self, arr, l, r, k):
        pos = self.randomized_partition(arr, l, r)
        num = pos - l + 1
        if k < num:
            self.randomized_selected(arr, l, pos - 1, k)
        elif k > num:
            self.randomized_selected(arr, pos + 1, r, k - num)

    def getLeastNumbers(self, arr, k):
        if k == 0:
            return list()
        self.randomized_selected(arr, 0, len(arr) - 1, k)
        return arr[:k]


if __name__ == '__main__':
    arr = [3, 2, 1, 1]
    k = 3
    print(Solution().getLeastNumbers(arr, k))

# 堆
# 快排选择
