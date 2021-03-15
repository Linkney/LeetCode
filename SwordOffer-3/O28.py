# Again 2020年11月13日09:45:35  二叉树
"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 判断以 root 为根节点的二叉树是否是镜像对称的
        # 如果是空节点 那么就是对称的   或者说 如果是叶子节点 那也是对称的 即 无左右子树
        def recur(L, R):
            if L is None and R is None:
                return True
            if L is None or R is None or L.val != R.val:
                return False

            return recur(L.left, R.right) and recur(L.right, R.left)

        if root is None:
            return True
        return recur(root.left, root.right)

# 做递归思考三步：
#
# 递归的函数要干什么？
# 函数的作用是判断传入的两个树是否镜像。
# 输入：TreeNode left, TreeNode right
# 输出：是：true，不是：false
# 递归停止的条件是什么？
# 左节点和右节点都为空 -> 倒底了都长得一样 ->true
# 左节点为空的时候右节点不为空，或反之 -> 长得不一样-> false
# 左右节点值不相等 -> 长得不一样 -> false
# 从某层到下一层的关系是什么？
# 要想两棵树镜像，那么一棵树左边的左边要和二棵树右边的右边镜像，一棵树左边的右边要和二棵树右边的左边镜像
# 调用递归函数传入左左和右右
# 调用递归函数传入左右和右左
# 只有左左和右右镜像且左右和右左镜像的时候，我们才能说这两棵树是镜像的
# 调用递归函数，我们想知道它的左右孩子是否镜像，传入的值是root的左孩子和右孩子。这之前记得判个root==null。
