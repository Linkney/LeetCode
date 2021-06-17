# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 节点数量范围 [0, 50]
        # Node.val  [-100, 100]

        # 递归方法解
        # if l1 is None:
        #     return l2
        # elif l2 is None:
        #     return l1
        # elif l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2

        # 普通人思路解
        prehead = ListNode(-1)  # NOT IMPORTANT

        travel = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                travel.next = l1
                l1 = l1.next
            else:
                travel.next = l2
                l2 = l2.next
            travel = travel.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        travel.next = l1 if l1 else l2

        return prehead.next

