"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树
如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树

示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 可以用上一题的方法 做 left 和 right 的 差值 绝对值
# 后序遍历 + 剪枝
# 树的深度 = max（左子树深度， 右子树深度） + 1
class Solution:
    # 后序遍历 + 剪枝 （从底至顶）
    # 思路是对二叉树做后序遍历，从底至顶返回子树深度，若判定某子树不是平衡树则 “剪枝” ，直接向上返回。
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            # 当节点 root 左右子树深度差 小于等于 1 时 返回 当前 root 为根的子树深度
            #                            大于等于 2 时 返回 -1  即 不是 平衡二叉树
            if not root:
                return 0
            left = recur(root.left)
            if left == -1:
                return -1
            right = recur(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1


class Solution55I:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)

    # 获取当前子树的深度的函数 depth(root)
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

