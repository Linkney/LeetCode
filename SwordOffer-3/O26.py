# Again 2020年11月11日11:12:00 二叉树匹配
"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:
     3
    / \
   4   5
  / \
 1   2

给定的树 B：
   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 输入两棵树 进行check是否符合   A主树 B小树
    def check(self, A, B):
        if B is None:
            return True
        if A.val != B.val or A is None:
            return False
        ans1 = self.check(A.left, B.left)
        ans2 = self.check(A.right, B.right)
        return ans1 and ans2

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None or B is None:
            return False

        ans1 = self.isSubStructure(A.left, B)
        ans2 = self.isSubStructure(A.right, B)
        return self.check(A, B) or ans1 or ans2


if __name__ == '__main__':
    A = TreeNode(1)
    A.left = TreeNode(2)
    A.right = TreeNode(3)
    A.left.left = TreeNode(1)
    # A.left.right = TreeNode(2)

    B = TreeNode(3)
    # B.left = TreeNode(1)

    print(Solution().isSubStructure(A, B))

#     def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
#         def recur(A, B):
#             if not B: return True
#             if not A or A.val != B.val: return False
#             return recur(A.left, B.left) and recur(A.right, B.right)
#
#         return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
