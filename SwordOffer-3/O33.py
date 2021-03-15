# Again 2020年11月18日09:26:21 二叉搜索树
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，
否则返回 false。假设输入的数组的任意两个数字都互不相同

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：
输入: [1,6,3,2,5]
输出: false

示例 2：
输入: [1,3,2,6,5]
输出: true
"""


# 1.后序遍历定义： [ 左子树 | 右子树 | 根节点 ] ，即遍历顺序为 “左、右、根”
# 2.二叉搜索树定义： 左子树中所有节点的值 << 根节点的值；
#                  右子树中所有节点的值 >> 根节点的值；其左、右子树也分别为二叉搜索树
# 由 1 2 推出 [ 小 | 大 | 中 ]
#       其中 小  大  递归判断 内部 [ 小 | 大 | 中 ]
class Solution:
    # def verifyPostorder(self, postorder: List[int]) -> bool:
    def verifyPostorder(self, postorder):
        # 判断 下标 i 和 j 之间的数据 是不是 符合题目要求
        def recur(i, j):
            # 单独一个数
            if i >= j:
                return True

            p = i
            # 小的都过掉
            while postorder[p] < postorder[j]:
                p += 1
            # 大的都过掉
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            # 小的大的都过掉是不是就能到达 根
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)

