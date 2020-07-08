"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：
给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        it = self
        ans = ''
        while it is not None:
            # print(it.val, '->', end='')
            ans = ans + str(it.val) + '->'
            it = it.next
        return ans[:-2]


class Solution:
    def reverse(self, head: ListNode, tail: ListNode):
        """
        # 翻转一个链表
        :param head: 头结点
        :param tail: 尾结点
        :return: 新头 新尾
        """
        prev = tail.next        # !!!!!  这个就非常夸张了 指针即一切
        p = head
        while prev != tail:
            nex = p.next
            # 头 搞到 尾巴上
            p.next = prev
            # 尾巴前提一格
            prev = p
            # 头往后推一格
            p = nex
        # 尾巴 变 头 ，  头 变 尾巴
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 头前面 的 头发
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            # 只要 头 不为空
            # 设置 尾部 和 头发部 相同 尾部 后推 每次只要找 尾巴 然后 确定 尾尾 即可
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            # pre , head, ....., tail , nex
            head, tail = self.reverse(head, tail)

            # 把翻转后的子链表重新接回原链表
            pre.next = head
            tail.next = nex

            # 已确定头 头发
            pre = tail
            head = tail.next

        return hair.next


if __name__ == '__main__':
    example = ListNode(1)
    example.next = ListNode(2)
    example.next.next = ListNode(3)
    example.next.next.next = ListNode(4)
    example.next.next.next.next = ListNode(5)
    # k = 2
    k = 3

    s = Solution()
    Ans = s.reverseKGroup(example, k)
    # Ans, _ = s.reverse(example, example.next, example.next.next.next.next)

    print(Ans)

    print("Finish")

