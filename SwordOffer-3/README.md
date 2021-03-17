# 三周目
## 标准：完全重刷 Code From Scratch

---

> #### O03 数组中重复的数字
>> - 萝卜坑
>> - ~~排序~~
>> - HashTable  
---
> #### O04 二维数组中查找
>> - 以左下角 或者 右上角 为起点 flag
>>     - 若 target > flag 则 可以消去一列
>>     - 若 target < flag 则 可以消去一行
---
> #### ~~O05 替换空格~~
---
> #### ~~O06 倒序打印链表~~
>> - ~~辅助栈~~
>> - 递归 ` return self.reversePrint(head.next) + [head.val] if head else [] `
---
> #### O07 通过前序遍历和中序遍历重建二叉树
>> ```
>> buildTree(data)
>>     if len(data) == 0: return None
>>     ans = TreeNode(data)
>>     ans.left = buildTree(leftdata)
>>     ans.right = buildTree(rightdata)
>>  ```
---
> #### ~~O09 用两个栈实现队列~~
---
> #### ~~O10-I 斐波那契数列~~
---
> #### ~~O10-II 青蛙跳台阶~~
---
> #### O11 旋转数组的最小数字 
>> - ~~顺序遍历寻找逆序对~~
>> - 二分查找
>>     - left <= (left + right) // 2 < right
>>     - 特例 \[1, 2, 3..., max] 旋转了 0 或者 全部 元素 需要  right 被向左拉
---
> #### O12 矩阵 DFS 
>> - 带 擦涂标记 的 dfs
>> ```
>> dfs(params):
>>     temp = data[x][y]
>>     data[x][y] = '/'
>>     ans = dfs(↑) or dfs(↓) or dfs(←) or dfs(→)
>>     date[x][y] = temp
>>     return ans
>> ```
---
> #### O13 矩阵 BFS
>> - Tips 1: 矩阵的 bfs 和 树结构的 bfs 略有不同 
>>     - 树 queue.put() 的元素 不会和 queue 里原有的元素重复
>>     - 矩阵 0,1 ↓ == 1,0 →
>> - Tips 2: set() 集合去重 
>>     - appearInQueue = set() 入队去重 
>>     - ans = set() 答案去重        _choice one in Tips 2_
>> ```
>> bfs(params):
>>     q = Queue()
>>     q.put(initData)
>>     while not q.empty():
>>         data = q.get()
>>         ...do sth about data...
>>         q.put(some data)
>>     return ans
>> ```
---
> #### ~~O014-I 剪绳子~~
>> m 能得到的最大乘积 = max\[（1,m-1) (2,m-2) ... (m/2, m/2) ]  问题的一步简化 m = x + y 转化为 递推
---
> #### ~~O014-II 剪绳子~~
>> 数学 驻点 = 2.7   得到切分规则
---
> #### O15  位运算
>> - & 按位与运算
>> - | 按位或运算
>> - ~ 按位翻转
>> - \>> 1 右移一位   相当于 除以2 取整 // 2
>> - \<< 1 左移一位
---
> #### O16 数值的整数次方 快速幂
>> `(m & 1) == 1`  即可判断奇偶性 妙哉
>> - 当 次数 为 偶数时： x 的 n 次 = x 平方 的 n // 2 次
>> - 当 次数 为 奇数时： x 的 n 次 = x 平方 的 n // 2 次 × 再乘上一个 x     再乘上的部分 暂存在 Ans 里
>> - 最简情况 次数 == 1 时： Ans = Ans * x 
---
> #### O17 打印从1到最大的n位数   大数打印法
>> - 大数表示 通过 String 类型
>> - 





---
> #### ~~O~~
---
> #### O
---