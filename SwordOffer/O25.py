"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(-1)
        work = ans

        while not(l1 is None or l2 is None):
            if l1.val >= l2.val:
                temp2 = l2.next
                work.next = l2
                l2 = temp2
            else:
                temp1 = l1.next
                work.next = l1
                l1 = temp1
            work = work.next
        if l1 is None:
            work.next = l2
        else:
            work.next = l1

        return ans.next
