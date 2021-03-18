# 妙哉
"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
"""

# A 原栈          | 9 10 7 3 5
# B 非严格降序    | 9 7 3
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mindata = []

    def push(self, x: int) -> None:
        if len(self.mindata) == 0:
            self.mindata.append(x)
        self.data.append(x)
        if self.mindata[-1] >= x:
            self.mindata.append(x)

    def pop(self) -> None:
        check = self.data.pop()
        if check == self.min():
            self.mindata.pop()

    def top(self) -> int:
        return self.data[-1]

    def min(self) -> int:
        return self.mindata[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

