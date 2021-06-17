"""
居合斩 二分法


基础组件：
    mid = ( left + right ) // 2
    mid = left + ( right - left ) // 2

        mid 中间偏左
        left(mid), right
        left, mid, right

    while left < right:
        # left, right 进入
        # left == right or right, left 出
        #       2 situation

        while 保证的逻辑   target 如果存在 只可能在   [left, right]  中    同时 不保证 是否存在边界上

"""


# 无重复 升序 数组 target 必然存在 查找 index
def midSearch1(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        # left(mid), right
        mid = (left + right) // 2
        # print("Index of left:{}, mid:{}, right:{}".format(left, mid, right))
        # print("Value of left:{}, mid:{}, right:{}, target:{}".format(nums[left], nums[mid], nums[right], target))
        # left right 都没有 check 所以出了 while left == right 需要进行最后一次 check
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # left mid right    --->    left -> right or right -> left 即  left == right    最后一个元素 待 check 即可
    # left(mid), right  --->
    #                  1. mid 较小     left -> right 即 left == right   同上
    #                  2. mid 较大     right, left   index 逆序 相当于 没找到 不需要 check 了  if left > right
    print("Out of while Index of left:{}, right:{}".format(left, right))
    if nums[left] == target:
        return left
    else:
        return -1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 3, 3, 4, 5]
    target1 = 4
    print(midSearch1(nums1, target1))

