"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead
分别完成在队列尾部插入整数和在队列头部删除整数的功能。 ( 若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
"""


# ____
# |  |              队头
# |  |
# |↓|    stackB    队尾       逆时针90°
#
# |  |              队头       顺时针90°
# |  |
# |__|    stackA    队尾    两个栈只能有一个存数据      规定 全在 stackB
class CQueue:
    def __init__(self):
        self.stackIn, self.stackOut = [], []        # 入队栈 & 出队栈

    def appendTail(self, value: int) -> None:
        self.stackIn.append(value)
        return

    def deleteHead(self) -> int:
        # 持续出队功能
        if self.stackOut:
            return self.stackOut.pop()
        # 出队栈为空
        # 将入队栈元素倒入出队栈 再出队
        while self.stackIn:
            self.stackOut.append(self.stackIn.pop())
        if self.stackOut:
            return self.stackOut.pop()
        # 两栈全空
        return -1

