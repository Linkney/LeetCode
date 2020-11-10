"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""


# Attention ： 地址赋值 ！
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 双指针 不断 逆向 下移
        # 初值启动仪表盘
        prev = None
        mid = head
        # 油门
        while mid is not None:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        return prev



