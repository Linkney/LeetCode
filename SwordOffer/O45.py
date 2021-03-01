# Again 2020年11月26日16:32:23
"""
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个

示例 1:
输入: [10,2]
输出: "102"

示例 2:
输入: [3,30,34,5,9]
输出: "3033459"
"""
import functools


class Solution:
    # def minNumber(self, nums: List[int]) -> str:
    def minNumber(self, nums):
        def sort_rule(x, y):
            # 字符串的拼接
            a, b = x + y, y + x
            # 字符串的大小比较
            #       （即 可迭代对象的大小比较
            #           先比较两个对象的第0个元素，大小关系即为对象的大小关系
            #               如果相等则继续比较后续元素，先终止迭代的认为是小的）
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0
        # 转换成字符串形式
        strs = [str(num) for num in nums]
        # 字符串排序
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)


if __name__ == '__main__':
    # nums = [3, 30, 34, 5, 9]
    # print(Solution().minNumber(nums))

    a = '30' + '3'
    print(type(a))
    print(a)
    b = '3' + '30'
    print(type(b))
    print(b)

# 因果 凉暗
