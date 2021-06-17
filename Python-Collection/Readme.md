## Python算法常用集合、库函数

- list
    - nums = list(set(nums))    去重
    - nums.sort()               排序
    - nums.sort( key=None, reverse=False)
        - nums.sort(key=lambda x: x\[第几个参数下标])
        - list.sort可以指定参数key，key接收一个函数。key函数只有一个参数
        - sort会对列表的每一个元素e调用key(e)，key(e)的返回值就是list.sort排序的依据
        - 对tuple进行排序，先按照第一个元素升序，如果第一个元素相同，再按照第二个元素降序排列
        - nums.sort(key=lambda x: (x\[0], -x\[1]))
    - pop()     # default last -1
    - append()
    - .index()     查找参数值 返回 index 下标

- set
    - s = set()
    - s.add()
    - s.remove()
    - len(s)
    - s.clear()
    - x in s

- permutations 全排列
    - import itertools
    - ans = list(itertools.permutations(listOfPer))
    
- dict
    - del dict\['keyName']  # 删除键 'Name'
    - dict.clear()          # 清空字典
    - len()
    - .copy()
    - key in dict
    - .get(key, default=None)   # 返回指定键的值，如果键不在字典中返回 default 设置的默认值
    - for key in sorted(dict) 
    - dict,keys()               # 返回一个迭代器，可以使用 list() 来转换为列表
    - .values()

- bisect
    - from bisect import bisect
    - index = bisect(listOfNums, Num)   查找Num在listOfNums中的插入位置
    
- Queue
    - from queue import Queue
    - queue = Queue()   
    - queue.put()       存数据
    - queue.empty()     判断是否为空
    - queue.get()       取数据
    - queue.qsize()     获取元素个数

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


- ord()     # 字符作为参数 返回对应的 ASCII 数值，或者 Unicode 数值
- chr()     # 反之


- import math
    - log
    - ceil




- 进制转换
    - int(input(), 16)
    - int(input(), 10)
    - int(input(). 8)
    

- f-string
    - 以 f 或 F 修饰符引领的字符串（f'xxx' 或 F'xxx'），以大括号 {} 标明被替换的字段
    - >>> name = 'Eric'
    - >>> f'Hello, my name is {name}'
    - 'Hello, my name is Eric'

- str.isdigit()
- str.islower()
- str.isupper()

- str.count(str)
    - str.count(sub, start= 0,end=len(string))
    - sub -- 搜索的子字符串
    - start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
    - end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。





- sort 和 sorted
    - sort 与 sorted 区别：
        - sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作
        - list 的 sort 方法返回的是对已经存在的列表进行操作
        - 而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作








#### Tips:
- bfs代码框架
    while queue 非空:
	node = queue.pop()
    for node 的所有相邻结点 m:
        if m 未访问过:
            queue.push(m)

    depth = 0 # 记录遍历到第几层
    while queue 非空:
        depth++
        n = queue 中的元素个数
        循环 n 次:
            node = queue.pop()
            for node 的所有相邻结点 m:
                if m 未访问过:
                    queue.push(m)




- 层次遍历的index规律： 
    - 父节点index = （子节点 - 1） // 2       # 除二取余
    - 子节点index = 父节点 * 2 + 1 or 2

