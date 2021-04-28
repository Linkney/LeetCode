# 排序算法 Python实现


# 选择排序
#   小数前置
#   在未排序序列中找到最小元素，存放到排序序列的起始位置，


def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            # 遍历后部不断交换较小值 即 更新最小值
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


# 冒泡排序
#   大数沉底
def bubble_sort(nums):
    n = len(nums)
    # 进行多次循环
    for c in range(n):
        # 后部 c 个位置冒泡排序完毕
        for i in range(1, n - c):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
    return nums


# 插入排序
#   将数据不断插入前面部分已排序好的数组
def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        # 从排序完毕的部分从后往前遍历找到合适位置
        while i > 0 and nums[i - 1] > nums[i]:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
            i -= 1
    return nums


# 希尔排序
#   插入排序进阶版
#   增量序列 t1, t2, ...  tk = 1    按照增量序列进行 k 趟直接插入排序
def shell_sort(nums):
    n = len(nums)
    gap = n // 2
    while gap:
        for i in range(gap, n):
            while i - gap >= 0 and nums[i - gap] > nums[i]:
                nums[i - gap], nums[i] = nums[i], nums[i - gap]
                # 以 gap 为间隔的序列进行排序 i -= 进行完整排序
                i -= gap
        gap //= 2
    return nums


# 归并排序 <!>
#   把长度为 n 的输入序列分成长度 n/2 的子序列
#   对两个子序列采用归并排序
#   合并所有子序列
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    # 分
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    # 合并
    return merge(left, right)


# 合并两个 升序nums到一个中
def merge(left, right):
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    # 其中可能有一个 剩下 += [...]   另一个为 += []
    res += left[i:]
    res += right[j:]
    return res


# 快速排序
#   哨兵左右分隔大小 递归
def quick_sort(nums):
    n = len(nums)

    def quick(left, right):
        if left >= right:
            return nums
        # 哨兵
        pivot = left
        i = left
        j = right
        # 左右比较大小 如果符合 刚好不动  指针向前滑行   找到两个都不符合 交换
        while i < j:
            while i < j and nums[j] > nums[pivot]:
                j -= 1
            # <= pivot 在第一位保持不动
            while i < j and nums[i] <= nums[pivot]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        # i == j 与 pivot 进行交换 交换到 index = 0 位置 （因为while中j先滑动 j先向i逼近）
        nums[pivot], nums[j] = nums[j], nums[pivot]
        quick(left, j - 1)
        quick(j + 1, right)
        return nums

    return quick(0, n - 1)


import random
# 随机快排
class RandomQucikSort:
    def randomized_partition(self, nums, l, r):
        # 随机 pivot index      l .... r(pivot)
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        # i [j .... ] r(pivot)
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        # small ...  small(i)   big .... big(j) r(pivot)
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        # small .... pivot(i) ... big
        return i

    def randomized_quicksort(self, nums, l, r):
        if r - l <= 0:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums):
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums


# 堆排序  todo
#   建堆，从底向上调整堆，使得父亲节点比孩子节点值大，构成大顶堆；
#   交换堆顶和最后一个元素，重新调整堆。
def heap_sort(nums):
    # 调整堆
    # 迭代写法
    def adjust_heap(nums, startpos, endpos):
        newitem = nums[startpos]
        pos = startpos
        childpos = pos * 2 + 1
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and nums[rightpos] >= nums[childpos]:
                childpos = rightpos
            if newitem < nums[childpos]:
                nums[pos] = nums[childpos]
                pos = childpos
                childpos = pos * 2 + 1
            else:
                break
        nums[pos] = newitem

    # 递归写法
    def adjust_heap(nums, startpos, endpos):
        pos = startpos
        chilidpos = pos * 2 + 1
        if chilidpos < endpos:
            rightpos = chilidpos + 1
            if rightpos < endpos and nums[rightpos] > nums[chilidpos]:
                chilidpos = rightpos
            if nums[chilidpos] > nums[pos]:
                nums[pos], nums[chilidpos] = nums[chilidpos], nums[pos]
                adjust_heap(nums, pos, endpos)

    n = len(nums)
    # 建堆
    for i in reversed(range(n // 2)):
        adjust_heap(nums, i, n)
    # 调整堆
    for i in range(n - 1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        adjust_heap(nums, 0, i)
    return nums


# 计数排序
#   空间换时间
#   找出待排序的数组的最大值和最小值
#   统计数组值的个数
#   反向填充目标数组
def counting_sort(nums):
    if not nums:
        return []
    n = len(nums)
    _min = min(nums)
    _max = max(nums)
    # index = [min, min+1, .... max]
    # 得到计数数组
    tmp_arr = [0] * (_max - _min + 1)
    for num in nums:
        tmp_arr[num - _min] += 1

    # 由计数数组调整排序后的数组
    j = 0
    for i in range(n):
        while tmp_arr[j] == 0:
            j += 1
        nums[i] = j + _min
        tmp_arr[j] -= 1
    return nums


# 桶排序
#   桶排序是计数排序的升级版   （计数排序 bucketSize == 1）
#   将数据分到有限数量的桶里，每个桶再分别排序
def bucket_sort(nums, bucketSize):
    if len(nums) <= 1:
        return nums
    _min = min(nums)
    _max = max(nums)
    # 需要桶个数
    bucketNum = (_max - _min) // bucketSize + 1
    buckets = [[] for _ in range(bucketNum)]
    for num in nums:
        # 放入相应的桶中
        buckets[(num - _min) // bucketSize].append(num)
    res = []
    for bucket in buckets:
        if not bucket:
            continue
        if bucketSize == 1:
            res.extend(bucket)
        else:
            # 当都装在一个桶里,说明桶容量大了
            if bucketNum == 1:
                bucketSize -= 1
            res.extend(bucket_sort(bucket, bucketSize))
    return res


# 基数排序   todo
#   基数排序是对数字每一位进行排序，从最低位开始排序
#   找到数组最大值，得最大位数；
#   从最低位开始取每个位组成radix数组；
#   对radix进行计数排序（计数排序适用于小范围的特点）
def Radix_sort(nums):
    if not nums:
        return []
    _max = max(nums)
    # 最大位数
    maxDigit = len(str(_max))
    bucketList = [[] for _ in range(10)]
    # 从低位开始排序
    div, mod = 1, 10
    for i in range(maxDigit):
        for num in nums:
            bucketList[num % mod // div].append(num)
        div *= 10
        mod *= 10
        idx = 0
        for j in range(10):
            for item in bucketList[j]:
                nums[idx] = item
                idx += 1
            bucketList[j] = []
    return nums


# Soltion -- 最小编辑距离
s1 = input()
s2 = input()
n = len(s1) + 1
m = len(s2) + 1
# dp[i][j] ： 表示 s1 的前 i 个 和 s2 的前 j 个的最小编辑距离   dp 起点为 空 对 空
dp = [[0] * m for i in range(n)]
# init
for i in range(n):
    dp[i][0] = i
for j in range(m):
    dp[0][j] = j
for i in range(1, n):
    for j in range(1, m):
        # index 错位一个 实际上 如果相等 就 传递 ↘ 不然则 min → ↓增加或删除操作 ↘ 更改操作+ 1
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

print(dp[-1][-1])
