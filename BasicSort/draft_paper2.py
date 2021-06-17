import numpy as np

class POINT:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class POLYGON:
    def __init__(self, points_num, points):
        self.points_num = points_num
        self.points = points        # 顺时针 或者 逆时针排序


def coss_multi(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]


def polygon_get_area(polygon):
    n = polygon.points_num

    if n < 3:
        return 0

    vectors = np.zeros((n, 2))
    for i in range(0, n):
        # vectors[i, :] = polygon[i, :] - polygon[0, :]
        vectors[i, :] = [polygon.points[i].x - polygon.points[0].x, polygon.points[i].y - polygon.points[0].y]

    area = 0
    for i in range(1, n):
        area = area + coss_multi(vectors[i - 1, :], vectors[i, :]) / 2

    return area


if __name__ == '__main__':
    p1 = POINT(0, 0)
    p2 = POINT(2, 0)
    p3 = POINT(2, 2)
    p4 = POINT(1, 3)
    p5 = POINT(0, 2)
    polygon = POLYGON(5, [p1, p2, p3, p4, p5])
    print(polygon_get_area(polygon))
