# 蛇形打印 1-2-4-7-5-3-6-8-9
# nums = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]
nums = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]

# start 0, 0  end -1, -1

# 行列
x, y = 0, 0
endX, endY = len(nums)-1, len(nums[0])-1            # index 0..len -1

# 右上 左下
order = [[-1, 1], [1, -1]]

# 上一次刚接触了边界 flag = 0 关闭  斜着走后 flag = 1开启
flag = 1

# 0 1
orderIndex = 0
ans = []
print("endX:", endX, "   endY:", endY)

# (x, y) != (endX, endY)
# 如果 x,y 不为 endX, endY 则 执行 True
while x != endX or y != endY:
    print("x, y :", x, y, "    orderIndex:", orderIndex, "   flag:", flag)
    ans.append(nums[x][y])

    # 边界检测
    if flag == 1:
        if x == 0 or x == endX or y == 0 or y == endY:
            flag = 0
            if x == 0 and y == endY:
                print("右上角")
                x += 1
                orderIndex = (orderIndex + 1) % 2
                continue
            if x == endX and y == 0:
                print("左下角")
                y += 1
                orderIndex = (orderIndex + 1) % 2
                continue
            if x == 0:
                print("上边界")
                y += 1
                orderIndex = (orderIndex + 1) % 2
                continue
            if y == 0:
                print("左边界")
                x += 1
                orderIndex = (orderIndex + 1) % 2
                continue
            if x == endX:
                print("下边界")
                y += 1
                orderIndex = (orderIndex + 1) % 2
                continue
            if y == endY:
                print("右边界")
                x += 1
                orderIndex = (orderIndex + 1) % 2
                continue

    # 非边界情况
    x += order[orderIndex][0]
    y += order[orderIndex][1]
    flag = 1

ans.append(nums[x][y])

print(ans)
print("-".join(map(str, ans)))
