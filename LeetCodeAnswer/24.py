"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# def swapPairs(self, head: ListNode) -> ListNode:
class Solution:
    def swapPairs(self, head):
        AnsPre = ListNode(-1)
        AnsPre.next = head

        prev_node = AnsPre

        # prev - first - second  交换 first 和 second
        while head and head.next:
            # 待交换的 两个节点
            first_node = head
            second_node = head.next

            # 交换 （这不是和直接交换 2 个数值 没啥区别么）
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # next 数据整理
            prev_node = first_node
            head = first_node.next

        return AnsPre.next


if __name__ == '__main__':
    example = ListNode(1)
    example.next = ListNode(2)
    example.next,next = ListNode(3)
    example.next.next.next =  ListNode(4)
    s = Solution()
    s.swapPairs(example)
