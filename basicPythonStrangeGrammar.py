"""
    奇怪的语法
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def trueOrFalse():
    # if (statement)
    #      statement 为一个 bool 值
    #             bool(a is b)
    if 1:
        print("if 1")
    if 0:
        print("if 0")
    if None:
        print("if None")
    if not None:
        print("if not None")
    A = None
    if A:
        print("if A(None)")
    if not A:
        print("if not A(None)")
    if A is None:
        print("if A(None) is None")
    if A is not None:
        print("if A(None) is not None")


if __name__ == '__main__':
    trueOrFalse()
