"""
请定义一个队列并实现函数 max_value 得到队列里的最大值
要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：
输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]

示例 2：
输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
"""
import queue


# 一个队列 + 一个双端队列（用来辅助存储max信息）
# 想象动画的过程
class MaxQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()    # 双端队列

    def max_value(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        # 更新 max 双端队列
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        # 其实就是 append
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1

        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

if __name__ == '__main__':
    maxQueue = MaxQueue()
    # ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
    # [[],[1],[2],[],[],[]]
    print(maxQueue.max_value())
    maxQueue.push_back(1)
    maxQueue.push_back(2)
    print(maxQueue.max_value())
    print(maxQueue.pop_front())
    print(maxQueue.max_value())
