"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
还有一个 random 指针指向链表中的任意节点或者 null。

示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

示例 3：
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

示例 4：
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# 两次遍历不就完事了么
#       第一次 构建 原始 链表
#       第二次 补充 Random
class Solution:
    # def copyRandomList(self, head: 'Node') -> 'Node':
    def copyRandomList(self, head):
        work1 = head
        work2 = head
        ansPrev = Node(-1)
        ansWork1 = ansPrev
        ansWork2 = ansPrev
        # id 对应表
        idLink = {}
        # 常规结构复制  并 保存新旧节点的对应 id
        while work1:
            temp = Node(work1.val)
            # 存对应关系
            idLink[work1] = temp
            ansWork1.next = temp
            work1 = work1.next
            ansWork1 = temp
        # Random next 复制
        #       ansWork2 进入工作状态
        ansWork2 = ansWork2.next
        while work2:
            if work2.random:
                temp = idLink[work2.random]
            else:
                temp = None
            ansWork2.random = temp
            work2 = work2.next
            ansWork2 = ansWork2.next

        return ansPrev.next


def show(l):
    temp = l
    while temp:
        random = "*"
        if not temp.random:
            random = "None"
        else:
            random = str(temp.random.val)
        print("[" + str(temp.val) + ", " + random + "]", end="")
        temp = temp.next
    print()


if __name__ == '__main__':
    l = Node(1)
    l.next = Node(2)
    l.next.next = Node(3)
    l.random = l.next.next
    l.next.random = l
    l.next.next.random = None
    # l.next.next.random = l

    show(l)

    getl = Solution().copyRandomList(l)
    show(getl)

# 上述方法被称为  哈希表 法 {}

# 拼接 + 拆分法
#       构造 原节点 1 -> 新节点 1 -> 原节点 2 -> 新节点 2 -> ……
#     if not head: return
#     cur = head
#     # 1. 复制各节点，并构建拼接链表
#     while cur:
#         tmp = Node(cur.val)
#         tmp.next = cur.next
#         cur.next = tmp
#         cur = tmp.next
#     # 2. 构建各新节点的 random 指向
#     cur = head
#     while cur:
#         if cur.random:
#             cur.next.random = cur.random.next
#         cur = cur.next.next       # 关键句
#     # 3. 拆分两链表        双双跳法
#     cur = res = head.next
#     pre = head
#     while cur.next:
#         pre.next = pre.next.next
#         cur.next = cur.next.next
#         pre = pre.next
#         cur = cur.next
#     pre.next = None # 单独处理原链表尾节点
#     return res      # 返回新链表头节点
