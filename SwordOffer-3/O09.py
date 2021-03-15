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
        self.stackA = []
        self.stackB = []

    def appendTail(self, value: int) -> None:
        self.stackB.append(value)
        return

    def deleteHead(self) -> int:
        if len(self.stackB) == 0:
            return -1

        # 将 stackB 全部倒入 stackA
        while len(self.stackB) > 0:
            item = self.stackB.pop()
            self.stackA.append(item)

        ans = self.stackA.pop()

        # 将stackA 再全部倒回去
        while len(self.stackA) > 0:
            self.stackB.append(self.stackA.pop())

        return ans

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

# 有个可以优化的点  连续 出队
