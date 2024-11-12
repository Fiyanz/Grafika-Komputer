import matplotlib.pyplot as plt
import modul.bezier as bzr


def plot_bzier_liner(bzr: list) -> None:

    x_coords = [point[0] for point in bzr]
    y_coords = [point[1] for point in bzr]

    plt.figure(figsize=(6, 6))
    plt.plot(x_coords, y_coords, marker='o', color='blue', markersize=5, linestyle='-', linewidth=1)
    plt.title("Plot Titik Perpindahan Algoritma Bezier Liner")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == "__main__":
    delta_t = 0.2
    points = [
        (1,4),
        (5,9)
    ]
    bzr_liner = bzr.linier(delta_t, points)
    plot_bzier_liner(bzr_liner)