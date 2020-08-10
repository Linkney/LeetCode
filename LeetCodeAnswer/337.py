"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:
输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        # ls表示偷左孩子能带来的最大收益，ln表示不偷左孩子能带来的最大收益，rs、rn同理
        # 情况1：    root 选     则 左右孩子不能选     即 root.val + ln + rn
        # 情况2：    root 不选   则 左右孩子选不选都行 即 max(ls, ln) + max(rs, rn)
        # 左右子树的选择情况 只通过 root 会产生相互影响
        def _rob(root):
            if not root:
                return 0, 0

            ls, ln = _rob(root.left)
            rs, rn = _rob(root.right)
            # 单个叶子节点 ls ln rs rn 都为 0  最终 return  ( root.val, 0 )
            return root.val + ln + rn, max(ls, ln) + max(rs, rn)

        return max(_rob(root))


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(5)
    root.right.right = TreeNode(1)
    print(Solution().rob(root))
