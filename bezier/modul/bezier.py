from math import comb

def _bezierf(t: float, p0: int, p1: int) -> float:
    """
    t: delta t
    p0: kordinat awal
    p1: kordinat akhir
    """
    return ((1 - t) * p0) + (t * p1)

def _bezier_n(t: float, points: list) -> float:
    """
    t: delta t
    points: titik kordinat
    """
    n = len(points)

    x = 0.0
    y = 0.0

    for i in range(n):
        basis = comb(n, i) * ((1 - t) ** (n - i)) * (t**i)
        x += basis * points[i][0]
        y += basis * points[i][1]

    return x, y



def bezier_linier(delta_t: float, points: list) -> list:
    """
    delta_t: nilai dari delta t
    points: list

    Note: hanya bisa untuk panjang list 2

    example:
        [(x0, y0), (x1, y1)]
    """
    point = []

    t = 0.0
    while t <= 1:

        x0 = points[0][0]
        y0 = points[0][1]

        x1 = points[1][0]
        y1 = points[1][1]

        x = _bezierf(t, x0, x1)
        y = _bezierf(t, y0, y1)

        point.append((x, y))

        t += delta_t

    return point



def bezier_kuadratik(alpaa_t: float, points: list) -> list:
    """
    alapa_t: berapa jarak
    points: kordinat
    """
    t = 0.0
    point = []

    # 0 <= t <= 1
    while t <= 1:
        x, y = _bezier_n(t, points)
        point.append((x, y))

        t += alpaa_t
    return point

if __name__ == "__main__":
    delta = 0.2
    linier_list = [
        (1, 2),
        (11, 12)
    ]

    point = [
            (1, 2),
            (7, 10),
            (15, 4)
            ]

    print("Bezer: ")
    print(bezier_kuadratik(delta, point))
    print("Bezer Linier: ")
    print(bezier_linier(delta, linier_list))
