"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""

# 前序遍历 [ 根 | 左 | 右 ]
# 中序遍历 [ 左 | 根 | 右 ]

"""
# 树的解题框架：
def traverse(TreeNode root):
    // 前序遍历
    traverse(root.left)
    // 中序遍历
    traverse(root.right)
    // 后序遍历
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    def buildTree(self, preorder, inorder):
        # 通过前序和后序建立 Tree

        # 特例 只有 根时候
        indexPreorder = -1


        return


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    Solution().buildTree(preorder, inorder)
