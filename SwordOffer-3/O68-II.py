# Again 2020年12月16日15:34:26  二叉树公共祖先
"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

                3
          5            1
      6      2      0      8
         7    4

示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 考虑通过递归对二叉树进行后序遍历，当遇到节点 p 或 q 时返回。从底至顶回溯
# 当节点 p, q 在节点 root 的异侧时，节点 root 即为最近公共祖先，则向上返回 root
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # 如果树为空，直接返回null
        if root is None:
            return None
        # 如果 p和q中有等于 root的，那么它们的最近公共祖先即为root（一个节点也可以是它自己的祖先）
        if root == p or root == q:
            return root
        # 递归遍历左子树，只要在左子树中找到了p或q，则先找到谁就返回谁
        left = self.lowestCommonAncestor(root.left, p, q)
        # 递归遍历右子树，只要在右子树中找到了p或q，则先找到谁就返回谁
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果在左子树中 p和 q都找不到，则 p和 q一定都在右子树中，
        # 右子树中先遍历到的那个就是最近公共祖先（一个节点也可以是它自己的祖先）
        if left is None:
            return right
        # 否则，如果 left不为空，在左子树中有找到节点（p或q），这时候要再判断一下右子树中的情况，
        # 如果在右子树中，p和q都找不到，则 p和q一定都在左子树中，
        # 左子树中先遍历到的那个就是最近公共祖先（一个节点也可以是它自己的祖先）
        elif right is None:
            return left
        # 否则，当 left和 right均不为空时，说明 p、q节点分别在 root异侧, 最近公共祖先即为 root
        else:
            return root


# 剑指offer
#   75/75  第一个书签  2020年12月16日16:16:03
