# Again 2020年12月16日15:16:41 二叉树
"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
        6
    2       8
  0   4   7   9
     3  5

示例 1:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。

示例 2:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # 迭代
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val < p.val and root.val < q.val:  # p,q 都在 root 的右子树中
                root = root.right  # 遍历至右子节点
            elif root.val > p.val and root.val > q.val:  # p,q 都在 root 的左子树中
                root = root.left  # 遍历至左子节点
            else:
                break
        return root

    # 递归
    def lowestCommonAncestor2(self, root, p, q):
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor2(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor2(root.left, p, q)
        return root
