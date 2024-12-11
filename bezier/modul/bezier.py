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
    n = len(points) - 1

    x = 0.0
    y = 0.0

    for i in range(n + 1):
        basis = comb(n, i) * ((1 - t) ** (n - i)) * (t**i)
        x += basis * points[i][0]
        y += basis * points[i][1]

    return x, y



def linier(delta_t: float, points: list) -> list:
    """
    Menghitung kordiat bezier linier
    Args:
    - delta_t: nilai dari delta t
    - points: list

    example:
        [(x0, y0), (x1, y1)]

    Return:
    - list points kordiat 

    Note: hanya bisa untuk panjang list 2
    """
    if len(points) > 3:
        raise ValueError("Kordinat harus kurang dari 3!!!")

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

def kuadratik(delta_t: float, points: list) -> list:
    """
    Menghitung titik-titik pada kurva Bézier kuadratik.

    Args:
    - points: list dari 3 koordinat titik kontrol [(x0, y0), (x1, y1), (x2, y2)]
    - delta_t: langkah perubahan nilai t (misalnya 0.01)

    Returns:
    - list_points: Daftar koordinat (x, y) pada kurva
    """
    if len(points) != 3:
        raise ValueError("Kurva Bézier kuadratik membutuhkan tepat 3 titik kontrol.")

    P0, P1, P2 = points
    list_points = []
    t = 0.0

    while t <= 1:
     
        x = (1 - t)**2 * P0[0] + 2 * (1 - t) * t * P1[0] + t**2 * P2[0]
        y = (1 - t)**2 * P0[1] + 2 * (1 - t) * t * P1[1] + t**2 * P2[1]
        
        list_points.append((x, y))
        t += delta_t

    return list_points


def kubik(delta_t: float, points: list) -> list:
    """
    Menghitung kuarva kubik

    Args:
    - points: list koordinat titik kontrol [(x0, y0), (x1, y1), (x2, y2), ..., (xn, yn)]
    - delta_t: langkah perubahan nilai t (misalnya 0.01)

    Returns:
    - list_points: Daftar koordinat (x, y) pada kurva
    """
    if len(points) <= 3:
        raise ValueError("Kordinat harus lebih dari 3 titik!!!")

    t = 0.0
    point = []

    # 0 <= t <= 1
    while t <= 1:
        x, y = _bezier_n(t, points)
        point.append((x, y))

        t += delta_t
    return point


