## Python算法常用集合、库函数

- set
    - s = set()
    - s.add()
    - s.remove()
    - len(s)
    - s.clear()
    - x in s

- permutations 全排列
    - import itertools
    - ans = list(itertools.permutations(listOfPer, len(listOfPer)))
    
- dict 

- bisect
    - from bisect import bisect
    - index = bisect(listOfNums, Num)   查找Num在listOfNums中的插入位置
    
- Queue
    - from queue import Queue
    - queue = Queue()
    - queue.put()
    - queue.empty()
    - queue.get()

- bin
    - 返回一个整数 int 或者长整数 long int 的二进制表示
        - bin(10)   输出   '0b1010'

- count
    - count() 方法用于统计字符串里某个字符出现的次数
    - str.count(sub, start= 0,end=len(string))

- eval
    - 执行一个字符串表达式，并返回表达式的值

- ceil
    - from math import ceil
    - ceil(num) 函数返回数字的上入整数
    - 正数 int(num)-1  负数 int(num)

- range
    - range(stop)
    - range(start, stop\[, step])

- re
    - import re

- [].pop
    - list.pop(index=-1)

#### Tips:
- 层次遍历的index规律： 
    - 父节点index = （子节点 - 1） // 2       # 除二取余
    - 子节点index = 父节点 * 2 + 1 or 2