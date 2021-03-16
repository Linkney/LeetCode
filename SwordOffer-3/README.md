# 三周目
## 标准：完全重刷 Code From Scratch

---

> #### O03 数组中重复的数字
>> - 萝卜坑
>> - ~~排序~~
>> - HashTable  


> #### O04 二维数组中查找
>> - 以左下角 或者 右上角 为起点 flag
>>     - 若 target > flag 则 可以消去一列
>>     - 若 target < flag 则 可以消去一行


> #### ~~O05 替换空格~~


> #### ~~O06 倒序打印链表~~
>> - ~~辅助栈~~
>> - 递归 ` return self.reversePrint(head.next) + [head.val] if head else [] `


> #### O07 通过前序遍历和中序遍历重建二叉树
>> ```
>> buildTree(data)
>>     if len(data) == 0: return None
>>     ans = TreeNode(data)
>>     ans.left = buildTree(leftdata)
>>     ans.right = buildTree(rightdata)
>>  ```


> #### ~~O09 用两个栈实现队列~~


> #### ~~O10-I 斐波那契数列~~


> #### ~~O10-II 青蛙跳台阶~~


> #### O11 旋转数组的最小数字 
>> - ~~顺序遍历寻找逆序对~~
>> - 二分查找
>>     - left <= (left + right) // 2 < right
>>     - 特例 [1, 2, 3..., max] 旋转了 0 或者 全部 元素 需要  right 被向左拉


> #### O12 DFS 
>> - 带 擦涂标记 的 dfs
>> ```
>> dfs(params):
>>     temp = data[x][y]
>>     data[x][y] = '/'
>>     ans = dfs(↑) or dfs(↓) or dfs(←) or dfs(→)
>>     date[x][y] = temp
>>     return ans
>> ```


> #### O13 BFS




> #### ~~O~~
> #### O