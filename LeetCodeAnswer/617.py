"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，
否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:
输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        # t1, t2 or None 即 其中有一个为 None 时就在这里 return 了不进递归了 另一个树的后面一整串直接嫁接过来
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        merged = TreeNode(t1.val + t2.val)
        merged.left = self.mergeTrees(t1.left, t2.left)
        merged.right = self.mergeTrees(t1.right, t2.right)
        return merged

    def showTree(self, t):
        if t is not None:
            print(t.val)
            self.showTree(t.left)
            self.showTree(t.right)
        return


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.left.left = TreeNode(5)
    t1.right = TreeNode(2)

    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.left.right = TreeNode(4)
    t2.right = TreeNode(3)
    t2.right.right = TreeNode(7)

    # 空
    print(id(t1.left.left.left))
    print(id(t1.left.left.right))

    print(t1.left.val)
    print(id(t1.left))
    print(t2.right.val)
    print(id(t2.right))

    t3 = Solution().mergeTrees(t1, t2)
    print(t3.left.left.val)
    print(id(t3.left.left))
    print(t1.left.left.val)
    print(id(t1.left.left))

    t3.left.left.val = 99
    print(t1.left.left.val)
