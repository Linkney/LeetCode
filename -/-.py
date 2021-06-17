# n = 3
# t = [1, 4, 7]
# h = [2, 5, 8]
# d = [3, 6, 9]
#
# ans = []
# # i 0 - n-1 实际上 1 - n
# for i in range(n):
#     icansee = 0
#     for j in range(n):
#         if j == i:
#             continue
#         else:
#             print(i, "->", j)
#             # i --> j check
#             # condition 1
#             cond1 = False
#             if t[i] - d[i] <= t[j] and t[j] <= t[i] + d[i]:
#                 cond1 = True
#             # condition 2
#             cond2 = True
#             for ij in range(min(i, j)+1, max(i, j)):
#                 if h[ij] >= h[j]:
#                     cond2 = False
#                     break
#
#             if cond1 and cond2:
#                 icansee += 1
#     ans.append(icansee)
#
# print(" ".join(map(str, ans)))


# n = 3
# t = [1, 4, 7]
# h = [2, 5, 8]
# d = [3, 6, 9]
#
# ans = []
# # i 0 - n-1 实际上 1 - n
# for i in range(n):
#     icansee = 0
#     for j in range(n):
#         if j == i:
#             continue
#         else:
#             # i --> j check
#             # print(i, "->", j)
#             # print(min(i, j) + 1, max(i, j))
#             cond1 = True
#             for ij in range(min(i, j) + 1, max(i, j)):
#                 if h[ij] >= h[j]:
#                     cond1 = False
#                     break
#             # print(cond1)
#             if cond1 and t[i] - d[i] <= t[j] <= t[i] + d[i]:
#                 icansee += 1
#
#     ans.append(icansee)
#
# print(" ".join(map(str, ans)))




n = 3
t = [1, 4, 7]
h = [2, 5, 8]
d = [3, 6, 9]

ans = []

for i in range(n):
    # i ->
    icansee = 0
    left = t[i] - d[i]
    right = t[i] + d[i]
    # 左

    for j in range(n):
        if i == j:
            continue
        else:
            if left <= t[j] <= right:
                cond1 = True
                for ij in range(min(i, j)+1, max(i, j)):
                    if h[ij] >= h[j]:
                        cond1 = False
                        break
                if cond1 is True:
                    icansee += 1

    ans.append(icansee)

print(" ".join(map(str, ans)))
