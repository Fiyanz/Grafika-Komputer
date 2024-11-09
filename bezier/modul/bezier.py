from math import comb

def bezierf(t: float, p0: int, p1: int) -> float:
    """
    t: delta t
    p0: kordinat awal
    p1: kordinat akhir
    """
    return ((1 - t) * p0) + (t * p1)

def bezier_linier(alpa_t: float, x1: int, y1: int, x2: int, y2: int) -> list:
    point = []

    t = 0.0


    while t <= 1:

        x = bezierf(t, x1, x2)
        y = bezierf(t, y1, y2)

        point.append((x, y))

        t += alpa_t

    return point


def bezier_n(t: float, points: list) -> float:

    n = len(points)

    x = 0.0
    y = 0.0

    for i in range(n):
        basis = comb(n, i) * ((1 - t) ** (n - i)) * (t**i)
        x += basis * points[i][0]
        y += basis * points[i][1]

    return x, y

def bezier_kuadratik(alpaa_t: float, points: list) -> list:
    """
    alapa_t: berapa jarak
    points: kordinat
    """
    t = 0.0
    point = []

    # 0 <= t <= 1
    while t <= 1:
        x, y = bezier_n(t, points)
        point.append((x, y))

        t += alpaa_t
    return point

# if __name__ == "__main__":
#     alpa = 0.02
#     x1, y1 = 1, 2
#     x2, y2 = 11, 12
#
#     point = [
#             (1, 2),
#             (7, 10),
#             (15, 4)
#             ]
#
#     print("Bezer: ")
#     print(bezier_kuadratik(alpa, point))
#     print("Bezer Linier: ")
#     print(bezier_linier(alpa, x1, y1, x2, y2))
