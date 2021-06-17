class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        hair = ListNode(-1)
        travel = hair

        add = 0
        # l1 和 l2 都不为空
        while l1 is not None and l2 is not None:
            sumval = l1.val + l2.val + add
            if sumval >= 10:
                add = 1
                sumval -= 10
            else:
                add = 0
            # 制作节点
            temp = ListNode(sumval)
            # 挂载
            travel.next = temp
            travel = travel.next
            l1 = l1.next
            l2 = l2.next
        # l1 或 l2 有剩余 或 add
        while l1:
            sumval = l1.val + add
            if sumval >= 10:
                add = 1
                sumval -= 10
            else:
                add = 0
            temp = ListNode(sumval)
            travel.next = temp
            travel = travel.next
            l1 = l1.next
        while l2:
            sumval = l2.val + add
            if sumval >= 10:
                add = 1
                sumval -= 10
            else:
                add = 0
            temp = ListNode(sumval)
            travel.next = temp
            travel = travel.next
            l2 = l2.next
        if add == 1:
            temp = ListNode(1)
            travel.next = temp
        return hair.next


if __name__ == '__main__':
    # l1  [9,9,9]
    # l2  [9,9]
    # ans [8,9,0,1]
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l2 = ListNode(9)
    l2.next = ListNode(9)

    ans = Solution().addTwoNumbers(l1, l2)
    while ans:
        print(ans.val)
        ans = ans.next
