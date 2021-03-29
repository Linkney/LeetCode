## Python IO 

#### Python 3
- input()
    - 接收一个标准 输入数据，返回为 string 类型
- map()
    - 根据提供的函数对指定序列做映射，返回function返回值 map object 可以使用 list() 包裹 
    - 数据只可被取走一次
    - map(function, iterable, ...)
- try except EOFError
    - 避免题目使用管道输入而报错
- strip()
    - 脱衣函数
- split()
    - 以空格间隔划分为列表
    - split(",")
- sorted()
    - sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作
    - 方法返回的是一个新的 list
    - sorted(iterable, key=None, reverse=False)  
- .join()
    - 用于将序列中的元素以指定的字符连接生成一个新的字符串
    - str.join(sequence)
- .sort()
    - 用于对原列表进行排序      原数据会变化
    - list.sort( key=None, reverse=False)
        - key -- 进行比较的元素，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
        - reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）







> 常用框架  循环输入没有 if 判断语句提供 break 使用 try expect break
```python
while True:
    try:
        a, b = map(int, input().strip().split())
        print(a + b)
    except EOFError:
        break

try:
    while True:
        a, b = map(int, input().strip().split())
        print(a + b)
except EOFError:
    pass
```
