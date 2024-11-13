import matplotlib.pyplot as plt
import modul.bezier as bzr


def plot_bzier(bzr: list) -> None:

    x_coords = [point[0] for point in bzr]
    y_coords = [point[1] for point in bzr]

    plt.figure(figsize=(6, 6))
    plt.plot(x_coords, y_coords, marker='o', color='blue', markersize=5, linestyle='-', linewidth=1)
    plt.title("Plot Titik Perpindahan Algoritma Bezier")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()



if __name__ == "__main__":
    delta_t = 0.02
    points = [
        (1,4),
        (5,9)
    ]

    points_kuadratik = [
        (3, 1), 
        (5, 3), 
        (10, 12)
    ]

    points_kubik = [
        (0, 3),
        (-4, 5),
        (10, 2),
        (4, -2),
        (-1, 0)
    ]

    bzr_liner = bzr.linier(delta_t, points)
    bzr_kuadratik = bzr.kuadratik(delta_t, points_kuadratik)
    bzr_kubik = bzr.kubik(delta_t, points_kubik)
    # plot_bzier(bzr_liner)
    # plot_bzier(bzr_kuadratik)
    plot_bzier(bzr_kubik)
