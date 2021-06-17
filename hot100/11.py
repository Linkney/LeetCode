'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai)
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水
'''


class Solution:
    # def maxArea(self, height: List[int]) -> int:
    def maxArea(self, height):
        # 容量 = min(h1, h2) * distance(h1, h2)
        # 一共有 n ^ 2 个容器

        # 状态太多 需要 消状态  （消去无意义状态）

        # 容量 = 宽度 * min(高度左， 高度右)
        # 遍历宽度 ? 宽度减少的同时 高度必须增加 不然没意义
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))
