l = ['a', 'c', 'b']
l.sort()
print(l)

# 小数除法
print(7/3)
# 取商
print(7//3)
# 取余
print(7 % 3)



l = [1, 2, 3]
print(l)
# print(','.join(l))       sequence item 0: expected str instance, int found
print(",".join(map(str, l)))

import itertools

listOfPer = [1, 2, 3]
per = list(itertools.permutations(listOfPer, len(listOfPer)))
print(per)



# 全排列 递归
def permutation(xs):   # 简化问题，假定形参xs是列表
    if len(xs) == 0 or len(xs) == 1:
        return [xs]
    result = []
    for i in xs:
        temp_list = xs[:]  # 对xs进行切片操作，使得temp_list的值和xs一样 但是temp_list的改变不影响xs
        temp_list.remove(i)     # 移除数值相等的值第一个值
        temp = permutation(temp_list)  # 使用递归 生成删掉一个元素的xs的全排列
        for j in temp:   # 对temp中的每一项再进行遍历
            j[0:0] = [i]   # 在index 0 的位置插入之前删去的i
            result.append(j)
    return result

print(permutation(listOfPer))


ans = [4, 3, 2, 1, 1]
ans.remove(1)
print(ans)
ans[0:0] = [99]
print(ans)



ans = 'abc123456'
print(ans[-6:])

print("------------------------------")

h = {}
todo = "bcaa"
s_todo = list(set(todo))
print(s_todo)
s_todo.sort()
print(s_todo)

print(todo)
for i in todo:
    print(i)
    if i in h:
        h[i] += 1
    else:
        h[i] = 1

print(h)

for i in h:
    print(i)
    print(h[i])

import bisect

a = [2, 3]
position = bisect.bisect(a, 2)
print(position)
# 用可变序列内置的insert方法插入
# a.insert(position, 2)
# print(a)
a[position] = 2
print(a)

print("=================================")
ans = "[\"a\",\"ab\",\"abc\",\"cd\",\"bcd\",\"abcd\"]"
get = eval(ans)
print(get)
print(get[0])

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range(8, 3):
    print(i)

print(0x7FFFFFFF)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
from math import ceil
print(ceil(3.2))
print(int(3.2)+1)
print(ceil(-3.2))
print(int(-3.2))
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
s = "adbca"
for l in range(len(s)-1, -1, -1):
    for r in range(l, len(s), 1):
        print("L:", l, "     R:",r)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range(0, -1, -1):
    print(i)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print(2**0)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print(5 // 2)     # 取整
print(5 % 2)      # 取余
print(3/7)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
import re
# pattern = re.compile(r"([()\+\*/-])")
s = "(2*(3-4))*5"
# s = re.split(pattern, s)
# print(s)


# 中缀表达式转后缀表达式 (2*(3-4))*5
def toBack(s):
    stack = []
    res = []
    d = {}
    d['+'] = 1
    d['-'] = 1
    d['*'] = 2
    d['/'] = 2
    d['('] = 0
    pattern = re.compile(r"([()\+\*/-])")
    s = re.split(pattern, s)
    for e in s:
        if e in '+-*/()':
            if e == "":
                continue
            if e == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    res.append(stack.pop())
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
            elif e == '(':
                stack.append(e)
            else:
                while len(stack) > 0 and d[stack[-1]] >= d[e]:
                    res.append(stack.pop())
                stack.append(e)
        else:
            res.append(e)
    res += stack[::-1]
    return res

print(toBack(s))

print("----------------------------------------------------")
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        queue = [root]
        ans = []

        while len(queue) > 0:
            print(queue)
            tempQueue = queue.copy()
            print(tempQueue)
            print(tempQueue[0])
            queue.clear()  # 将当前 queue 全部刷新
            print(queue)
            print(tempQueue)
            tempAns = []

            while len(tempQueue) > 0:
                print("while")
                print(tempQueue)
                temp = tempQueue.pop(0)
                print(temp)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)

                tempAns.append(temp.val)
            ans.append(tempAns)

        return ans


if __name__ == '__main__':
    ll = [1, 2, 3]

    print(ll[::-1])