class Solution:
    # def sortColors(self, nums: List[int]) -> None:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()

        # 0 .. 0 1 ... 1 2 ... 2

        index0 = 0
        index2 = len(nums) - 1
        # 如果 0 则放到 index0  index0++
        # 如果 2 则放到 index2  index2--  如果换出的来 不为 1  那么得回退 不能让他就这么过去了  i--
        # 如果 1 continue

        # python for 循环中 i 不能 修改 回退 使用 while
        i = 0
        # for i in range(len(nums)):
        while i <= len(nums):

            if i > index2:
                break

            if nums[i] == 0:
                nums[index0], nums[i] = nums[i], nums[index0]
                index0 += 1
            elif nums[i] == 1:
                i += 1
                continue
            else:
                nums[index2], nums[i] = nums[i], nums[index2]
                index2 -= 1
                if nums[i] != 1:
                    i -= 1

            i += 1
            print(nums)

        print("Ans:", nums)


if __name__ == '__main__':
    # nums = [2, 0, 1]
    nums = [1, 2, 0]
    Solution().sortColors(nums)
