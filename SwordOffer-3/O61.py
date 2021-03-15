"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字
A 不能视为 14。

示例 1:
输入: [1,2,3,4,5]
输出: True

示例 2:
输入: [0,0,1,2,5]
输出: True
"""


# 5个数 都必须用上 即 最小的常规数 必然已经决定了唯一正确顺子序列
class Solution:
    # def isStraight(self, nums: List[int]) -> bool:
    def isStraight(self, nums):
        nums.sort()
        # print(nums)
        magicNum = 0
        prevNum = -1
        i = 0
        while i < 5:
            # 一阶段记录大小王（可能存在）
            if nums[i] == 0:
                magicNum += 1
                i += 1
                continue
            # 二阶段正常数字
            #       第一个常规数字
            if prevNum == -1:
                prevNum = nums[i]
            else:
                if nums[i] != prevNum + 1:
                    # 不符合 prev num 且 没有 大小王备用
                    if magicNum == 0:
                        return False
                    magicNum -= 1
                    i -= 1
                # 前进
                prevNum += 1
            # print("prevNum:", prevNum, "      magicNum:", magicNum)
            i += 1
        return True


if __name__ == '__main__':
    nums = [0, 0, 1, 2, 7]
    print(Solution().isStraight(nums))
