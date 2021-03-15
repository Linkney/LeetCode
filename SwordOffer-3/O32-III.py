"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

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
  [20,9],
  [15,7]
]
"""


import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

        # 这再翻个个 闲的蛋疼
        for item in range(len(ans)):
            if item % 2 == 1:
                ans[item].reverse()
        return ans


if __name__ == '__main__':
    tr = TreeNode(3)
    tr.left = TreeNode(9)
    tr.right = TreeNode(20)
    tr.right.left = TreeNode(15)
    tr.right.right = TreeNode(7)

    print(Solution().levelOrder(tr))
