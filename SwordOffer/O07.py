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

        print("preorder:", preorder)
        print("inorder:", inorder)

        if len(preorder) == 0:
            print("In")
            return None
        # 从前序中得到根节点
        ans = TreeNode(preorder[0])

        # 在中序中找到分割
        index = inorder.index(preorder[0])
        inleftLen = index
        inorderLeft = inorder[:index]
        inorderRight = inorder[index+1:]
        # 在前序中分割出 左子树部分
        preorderLeft = preorder[1:1+inleftLen]
        preorderRight = preorder[1+inleftLen:]

        ans.left = self.buildTree(preorderLeft, inorderLeft)
        ans.right = self.buildTree(preorderRight, inorderRight)

        return ans


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    Solution().buildTree(preorder, inorder)
