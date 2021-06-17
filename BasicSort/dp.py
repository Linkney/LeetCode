# Soltion -- 最小编辑距离
s1 = input()
s2 = input()
n = len(s1) + 1
m = len(s2) + 1
# dp[i][j] ： 表示 s1 的前 i 个 和 s2 的前 j 个的最小编辑距离   dp 起点为 空 对 空
dp = [[0] * m for i in range(n)]
# init
for i in range(n):
    dp[i][0] = i
for j in range(m):
    dp[0][j] = j
for i in range(1, n):
    for j in range(1, m):
        # index 错位一个 实际上 如果相等 就 传递 ↘ 不然则 min → ↓增加或删除操作 ↘ 更改操作+ 1
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

print(dp[-1][-1])
