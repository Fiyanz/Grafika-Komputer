import numpy as np
import matplotlib.pyplot as plt
import modul.bezier as bzr
from matplotlib.widgets import Slider, Button
from mpl_toolkits.mplot3d import Axes3D


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

# Plotting Interaktif
def interactive_plot(points: list) -> None:
    # Titik awal
    points = points[:]
    delta_t = 0.02

    fig, ax = plt.subplots(figsize=(6, 6))
    plt.subplots_adjust(bottom=0.25)

    curve_line, = ax.plot([], [], 'b-', label='Bezier Curve')
    points_line, = ax.plot([], [], 'ro-', label='Control Points')
    ax.legend()

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True)
    ax.set_title("Interactive Bezier Curve")

    # Sliders
    t_slider_ax = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    t_slider = Slider(t_slider_ax, 'Delta t', 0.01, 0.1, valinit=delta_t, valstep=0.01)

    # Update fungsi
    def update(val):
        delta_t = t_slider.val
        curve = bzr_kubik(delta_t, points)
        curve_line.set_data(*zip(*curve))
        points_line.set_data(*zip(*points))
        fig.canvas.draw_idle()

    t_slider.on_changed(update)

    # Reset Button
    reset_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
    reset_button = Button(reset_ax, 'Reset', color='lightgoldenrodyellow', hovercolor='0.975')

    def reset(event):
        nonlocal points
        points = points[:]
        update(None)

    reset_button.on_clicked(reset)

    # Event handler untuk menggeser titik
    def on_click(event):
        if event.inaxes == ax:
            nonlocal points
            for i, (x, y) in enumerate(points):
                if abs(x - event.xdata) < 0.5 and abs(y - event.ydata) < 0.5:
                    points[i] = (event.xdata, event.ydata)
                    update(None)
                    break

    fig.canvas.mpl_connect('button_press_event', on_click)

    # Update awal
    update(None)
    plt.show()


if __name__ == "__main__":
    delta_t = 0.02

    points_kubik = [
        (0, 3),
        (-4, 5),
        (10, 2),
        (4, -2),
        (-1, 0)
    ]

    bzr_kubik = bzr.kubik(delta_t, points_kubik)
    # plot_bzier(bzr_kubik)
    interactive_plot(points_kubik)
    print(bzr_kubik)
