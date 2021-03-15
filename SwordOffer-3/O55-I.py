# Again 2020年12月8日19:21:08 二叉树的深度
"""
输入一棵二叉树的根节点，求该树的深度
从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度

例如：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树深度
#       1, 递归
#       2. 层次遍历
class Solution:
    # 递归     已该节点为根的树的深度
    def maxDepth1(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans1 = self.maxDepth1(root.left)
        ans2 = self.maxDepth1(root.right)
        return max(ans1, ans2) + 1

    # 层次遍历
    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue, res = [root], 0
        # 队列 入队 出队 加节点队列 刷新层次数  直到队列为空
        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            res += 1
        return res
