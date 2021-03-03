# Again 2020年11月18日17:09:18 二叉树回溯 （二叉树遍历 + 路径记录）
# Need to think clear
"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径
【Attention 直到叶节点为止】

示例:
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 本质上是一个 二叉树的回溯代码结构   挂载上 符合条件的路径记录
class Solution:
    # def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    def pathSum(self, root, sum):
        ans = []
        # 容器
        path = []

        # 递归 以 root 为根 目标值 为 tar
        def recur(root, tar):
            # 如果 root 为 None   这里的 return 非常关键 与 pop 构成回溯
            if not root:
                return

            # 通过该节点   路径记录
            path.append(root.val)
            tar -= root.val
            # 如果 目标值为 0 且 为 叶子节点  将当前路径 送入 答案框
            if tar == 0 and not root.left and not root.right:
                # list(path) 相当于新建并复制了一个 path 列表  （不能存引用 要存内存快照）
                ans.append(list(path))

            recur(root.left, tar)
            recur(root.right, tar)
            # 这个 回溯的 pop  这个 pop 位置 值得体会 和 思考
            path.pop()

        recur(root, sum)
        return ans

    # 二叉树先序遍历
    def _recur(self, root):
        if not root: return

        print(root.val)
        if not root.left and not root.right:
            print("挂载叶节点检测器")

        self._recur(root.left)
        self._recur(root.right)
        print("pop")
        return


if __name__ == '__main__':

    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.left.left = TreeNode(11)
    tree.left.left.left = TreeNode(7)
    tree.left.left.right = TreeNode(2)
    tree.right = TreeNode(8)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(4)
    tree.right.right.left = TreeNode(5)
    tree.right.right.right = TreeNode(1)
    Solution()._recur(tree)
