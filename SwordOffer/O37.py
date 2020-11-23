# Again 2020年11月23日10:42:13
"""
请实现两个函数，分别用来序列化和反序列化二叉树

示例: 
你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5, null, null, null, null]"
"""


# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        # 出队 塞左右子节点 记录答案
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return
        vals = data[1:-1].split(',')
        i = 1       # index of data str
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        # 一个节点 对应 两个序列化的str位置
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    tr = TreeNode(1)
    tr.left = TreeNode(2)
    tr.right = TreeNode(3)
    tr.right.left = TreeNode(4)
    tr.right.right = TreeNode(5)

    codec = Codec()
    print(codec.serialize(tr))
    ls = "[1,2,3,null,null,4,5,null,null,null,null]"
    ansTree = codec.deserialize(ls)
