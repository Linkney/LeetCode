"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：
[3,9,20,15,7]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树问题 天然的重复子结构   天然的函数作用定义 递归
# [ root, root.left, root.right]   不对劲
# 得 队列 辅助  队列里存这 一层的节点
class Solution:
    # def levelOrder(self, root: TreeNode) -> List[int]:
    def levelOrder(self, root):
        if not root:
            return []

        # 输入节点队列 返回新节点队列 和产生的中间 ans
        def next(queue):
            ansQueue = []
            ansLayer = []
            while len(queue) > 0:
                root = queue.pop(0)
                # todo ??????????????????  A is not None  和  not A 不一样 ????????
                # if root.left is not None:
                if root.left:
                    ansLayer.append(root.left.val)
                    ansQueue.append(root.left)
                # if root.right is not None:
                if root.right:
                    ansLayer.append(root.right.val)
                    ansQueue.append(root.right)
            return ansQueue, ansLayer

        queue = [root]
        ans = [root.val]
        while True:
            aq, al = next(queue)
            ans += al
            queue = aq
            if len(queue) == 0:
                break
        return ans


if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.left.right = TreeNode(100)
    tree.left.right.left = TreeNode(999)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    print(Solution().levelOrder(tree))


