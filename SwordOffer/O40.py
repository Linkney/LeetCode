"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]
"""


class Solution:
    # def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
    def getLeastNumbers(self, arr, k):
        # ? 这调用排序这不完事了
        arr.sort()
        # 还得去重
        # arrNoSame = []
        # for i in arr:
        #     if i not in arrNoSame:
        #         arrNoSame.append(i)

        return arr[0:k]


if __name__ == '__main__':
    arr = [3, 2, 1, 1]
    k = 3
    print(Solution().getLeastNumbers(arr, k))

# 堆
# 快排选择
