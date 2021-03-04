# Again 2020年12月8日19:41:56 二叉树
"""
给定一棵二叉搜索树，请找出其中第k大的节点

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 右  根  左  得到递减序列
        def dfs(root):
            if not root:
                return
            dfs(root.right)

            # print(root.val)   递减序列
            # 特殊情况 k = 0
            if self.k == 0:
                return

            self.k -= 1
            if self.k == 0:
                self.res = root.val

            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res
