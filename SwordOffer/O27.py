# Again 2020年11月12日17:08:14  二叉树
"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9

镜像输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BasicTree:
    def showTree(self, root):
        if root is not None:
            print("root.val:", root.val)
        else:
            print("root.val: None")
            return
        self.showTree(root.left)
        self.showTree(root.right)


class Solution:
    # def mirrorTree(self, root: TreeNode) -> TreeNode:
    def mirrorTree(self, root):
        # 函数功能：返回一个 镜像化（以root为根节点的二叉树） 的二叉树
        #       如果 节点为空 （都没有左右子树了 就不用镜像化了）
        #       root的right ， root的left = 镜像化 （root的left）  ，  镜像化 （root的right）
        if root is None:
            return None
        # 等式右边被打包成元组 同时赋值 给左侧多个变量
        root.right, root.left = self.mirrorTree(root.left), self.mirrorTree(root.right)
        # 等价于下面 3 行
        # tmp = root.left       # 左子树先存
        # root.left = self.mirrorTree(root.right)       # 新（镜像后）的树 的 左子树 是 右子树的镜像
        # root.right = self.mirrorTree(tmp)             # ---
        return root

#   1
# 2   3


if __name__ == '__main__':
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(7)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(9)

    bt = BasicTree()
    bt.showTree(tree)

    print("-----------------Mirror-----------------")
    mtree = Solution().mirrorTree(tree)
    bt.showTree(mtree)
