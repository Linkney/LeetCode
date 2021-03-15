"""
输入两个链表，找出它们的第一个公共节点。
如下面的两个链表：
在节点 c1 开始相交。

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构
可假定整个链表结构中没有循环
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 如果香蕉 则最后一个节点 一定是一样的
#       Distance 先发车  即 会相遇
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        oneA = headA
        oneB = headB

        # A 和 B 都非空的时候 就运行 （有一个空的时候就不运行了）
        while oneA.next is not None and oneB.next is not None:
            oneA = oneA.next
            oneB = oneB.next
        # 至少有一个为空了
        distans = 0
        # 两者一样长
        if oneA.next is None and oneB.next is None:
            if oneA == oneB:
                return oneA
            else:
                return None
        # B长
        if oneA.next is None and oneB.next is not None:
            while oneB is not None:
                distans += 1
                oneB = oneB.next
            if oneA != oneB:
                return None
            else:
                while distans > 0:
                    headA = headA.next
                while headA != headB:
                    headA = headA.next
                    headB = headB.next
                return headA
        # A长
        if oneB.next is None and oneA.next is not None:
            while oneA is not None:
                distans += 1
                oneA = oneA.next
            if oneA != oneB:
                return None
            else:
                while distans > 0:
                    headB = headB.next
                while headA != headB:
                    headA = headA.next
                    headB = headB.next
                return headA

        return headA

    def _getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        # 画个图就明白了 走两趟
        while node1 != node2:
            print("node1:", node1.val)
            print("node2:", node2.val)
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1


if __name__ == '__main__':
    A = ListNode(3)
    A.next = ListNode(2)

    B = ListNode(5)
    B.next = ListNode(4)

    # point = ListNode(1)
    # A.next.next = point
    # B.next.next = point

    print(Solution().getIntersectionNode(A, B))
    print(Solution()._getIntersectionNode(A, B))
