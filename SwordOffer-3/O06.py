"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def reversePrint(self, head: ListNode) -> List[int]:
    # 存链表 再倒序 打印
    def reversePrint(self, head):
        ans = []
        while head is not None:
            ans.append(head.val)
            head = head.next
        ans.reverse()
        return ans

    # 帅气的递归
    def reversePrint2(self, head):
        return self.reversePrint(head.next) + [head.val] if head else []


if __name__ == '__main__':
    linklist = ListNode(1)
    linklist.next = ListNode(3)
    linklist.next.next = ListNode(2)

    print(Solution().reversePrint2(linklist))
