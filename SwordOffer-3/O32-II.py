"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 这不是和上一题一样么
class Solution:
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    def levelOrder(self, root):
        if not root: return []

        queue = collections.deque()
        ans = []
        queue.append(root)
        while queue:
            temp = []
            # 直接把 Queue 里的全部弄了  用 for 记录了个数
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(temp)
        return ans


if __name__ == '__main__':
    tr = TreeNode(3)
    tr.left = TreeNode(9)
    tr.right = TreeNode(20)
    tr.right.left = TreeNode(15)
    tr.right.right = TreeNode(7)

    print(Solution().levelOrder(tr))
