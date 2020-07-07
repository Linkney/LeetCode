"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# def mergeKLists(self, lists: List[ListNode]) -> ListNode:
class Solution:
    def mergeKLists(self, lists):
        # 把所有的数字 拿出来 做个 排序 创建 数据结构即可
        temp = []
        for i in lists:
            # 遍历 list
            # 特例 [ None, ListNone , LisNode ]
            if i is None:
                continue
            while i.next is not None:
                # 遍历单个数据结构
                temp.append(i.val)
                i = i.next
            # 生了个尾巴
            temp.append(i.val)
        print(temp)
        temp.sort()
        print(temp)
        AnsPre = ListNode(-1)
        run = AnsPre
        for i in temp:
            addNode = ListNode(i)
            run.next = addNode
            run = addNode
        return AnsPre.next


if __name__ == '__main__':
    e1 = ListNode(1)
    e1.next = ListNode(4)
    e1.next.next = ListNode(5)
    e2 = ListNode(1)
    e2.next = ListNode(3)
    e2.next.next = ListNode(4)
    e3 = ListNode(2)
    e3.next = ListNode(6)
    example = [e1, e2, e3]

    s = Solution()
    ans = s.mergeKLists(example)
    while ans.next is not None:
        print(ans.val)
        ans = ans.next
    print(ans.val)


