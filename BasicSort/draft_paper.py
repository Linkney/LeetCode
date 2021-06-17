class POINT:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def cross(p1, p2, p3):
    x1 = p2.x - p1.x
    y1 = p2.y - p1.y
    x2 = p3.x - p1.x
    y2 = p3.y - p1.y
    return x1 * y2 - x2 * y1


def if_two_line_intersection(p1, p2, p3, p4):
    if max(p1.x, p2.x) >= min(p3.x, p4.x) and max(p3.x, p4.x) >= min(p1.x, p2.x) and \
            max(p1.y, p2.y) >= min(p3.y, p4.y) and max(p3.y, p4.y) >= min(p1.y, p2.y):
        if cross(p1, p2, p3) * cross(p1, p2, p4) <= 0 and cross(p3, p4, p1) * cross(p3, p4, p2) <= 0:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    i = "-1,2,-1,1"
    # -1 无依赖   -2 已完成
    work = list(map(int, i.split(",")))
    ans = []
    while len(ans) < len(work):
        # -1 √
        for i in range(len(work)):
            if work[i] == -1:
                ans.append(i)
                work[i] = -2
        print("work:", work)
        print("ans:", ans)
        # x -1
        for i in range(len(work)):
            if work[i] == -2:
                continue

            if work[work[i]] == -2:
                work[i] = -1

        print("work:", work)
        print("ans:", ans)

    print(",".join(map(str, ans)))


