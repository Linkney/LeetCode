"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1


返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 递归 输入节点 和 一个和值 输出是否有 路
        # 1.空节点 无路
        # 2.叶节点 判断是否相同
        # 中间结点（相对根节点） 其左右子节点是否有路  划分成 2个子问题 子问题的答案之间 为 或 关系

        # 边界  只有一个子节点时  的  None 分支 答案
        if root is None:
            return False

        cut = sum - root.val
        # 该节点是叶子节点
        if root.left is None and root.right is None:
            return not bool(cut)     # 0 False others True
        # todo 不知道为什么在 LeetCode 里报错
        # 中间节点 （左右 单左 单右） （单左 单右 且数据已经超了或相等 可以剪枝）
        # if ((root.right is None and root.left is not None) or (root.left is None and root.right is not None))\
        #         and cut <= 0:
        #     return False

        return self.hasPathSum(root.left, cut) or self.hasPathSum(root.right, cut)


if __name__ == '__main__':
    example = TreeNode(5)
    example.left = TreeNode(4)
    example.left.left = TreeNode(11)
    example.left.left.left = TreeNode(7)
    example.left.left.right = TreeNode(2)
    example.right = TreeNode(8)
    example.right.left = TreeNode(13)
    example.right.right = TreeNode(4)
    example.right.right.right = TreeNode(1)

    s = Solution()
    print(s.hasPathSum(example, 22))



