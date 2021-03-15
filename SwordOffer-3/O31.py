# 憨傻
"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，
序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

示例 1：
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

示例 2：
输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。
"""


# pop 出现一个数后  push 该数的前部 被 freeze
#       只能 一路向前 或者 随时向后 + 一路向前
#       山峰线特征：
#                   不能高度缺失降落
#    山峰线的数学理论 推进受阻


# 模拟栈 行为
class Solution:
    # def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    def validateStackSequences(self, pushed, popped):
        stack = []
        # poped 的游标
        i = 0
        for num in pushed:
            # num 入栈
            stack.append(num)
            # 循环判断与出栈  stack is not None 运行不通过  stack 运行通过
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        # stack     None   not None
        # return    True   False
        # 有出不掉的残留了 那就是 False 了
        return not stack

# None      0   False
# not None  1   True


if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]

    # pushed = [1, 2, 3, 4, 5]
    # popped = [4, 3, 5, 1, 2]
    print(Solution().validateStackSequences(pushed, popped))
