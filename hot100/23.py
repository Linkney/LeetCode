"""
合并k个升序链表
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    # 链表的数 全部存成 list 再 排序 再 转换成 链表
    def mergeKLists(self, lists):
        # 把所有的数字 拿出来 做个 排序 创建 数据结构即可
        temp = []
        for i in lists:
            # 遍历 list
            if i is None:
                continue
            while i.next is not None:
                # 遍历单个数据结构
                temp.append(i.val)
                i = i.next
            # 剩了个尾巴
            temp.append(i.val)

        temp.sort()

        AnsPre = ListNode(-1)
        run = AnsPre
        for i in temp:
            addNode = ListNode(i)
            run.next = addNode
            run = addNode
        return AnsPre.next

