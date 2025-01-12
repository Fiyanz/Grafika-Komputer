import  matplotlib.pyplot as plt
import modul.bezier as bzr
from matplotlib.widgets import Slider, Button, TextBox


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
    initial_points = points[:]
    delta_t = 0.01

    fig, ax = plt.subplots(figsize=(6, 6))
    plt.subplots_adjust(bottom=0.25)

    curve_line, = ax.plot([], [], 'b-', label='Bezier Curve')
    points_line, = ax.plot(*zip(*points), 'ro-', label='Control Points')
    ax.legend()

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True)
    ax.set_title("Interactive Bezier Curve")

    # Sliders
    t_slider_ax = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    t_slider = Slider(t_slider_ax, 'Delta t', 0.01, 1.0, valinit=delta_t, valstep=0.01)

    # Update fungsi
    def update(val):
        delta_t = t_slider.val
        curve = bzr.kubik(delta_t, points)
        curve_line.set_data(*zip(*curve))
        points_line.set_data(*zip(*points))
        fig.canvas.draw_idle()

    t_slider.on_changed(update)

    # Reset Button
    reset_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
    reset_button = Button(reset_ax, 'Reset', color='lightgoldenrodyellow', hovercolor='0.975')

    def reset(event):
        nonlocal points
        points.clear()
        points.extend(initial_points)
        update(None)

    reset_button.on_clicked(reset)

    # Event handler untuk menggeser titik
    selected_point = None

    def on_click(event):
        nonlocal selected_point
        if event.inaxes != ax:
            return
        for i, (x, y) in enumerate(points):
            if abs(x - event.xdata) < 0.5 and abs(y - event.ydata) < 0.5:
                selected_point = i
                print(f"Point {i} selected")
                break

    def on_motion(event):
        nonlocal selected_point
        if selected_point is None:
            return
        if event.inaxes != ax:
            return
        points[selected_point] = (event.xdata, event.ydata)
        print(f"Point {selected_point} moved to ({event.xdata}, {event.ydata})")
        update(None)

    def on_release(event):
        nonlocal selected_point
        print(f"Point {selected_point} released")
        selected_point = None

    fig.canvas.mpl_connect('button_press_event', on_click)
    fig.canvas.mpl_connect('motion_notify_event', on_motion)
    fig.canvas.mpl_connect('button_release_event', on_release)

    # Update awal
    update(None)
    plt.show()

def manual_point_plot() -> list:
    points = []
    fig, ax = plt.subplots(figsize=(6, 6))
    plt.subplots_adjust(bottom=0.25)

    points_line, = ax.plot([], [], 'ro-', label='Control Points')
    ax.legend()

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True)
    ax.set_title("Manual Point Plot - Click to Add Points")

    def update():
        if points:
            x_coords, y_coords = zip(*points)
            points_line.set_data(x_coords, y_coords)
        else:
            points_line.set_data([], [])
        fig.canvas.draw_idle()

    def on_click(event):
        if event.inaxes == ax:
            points.append((event.xdata, event.ydata))
            print(f"Added point: ({event.xdata:.2f}, {event.ydata:.2f})")
            update()

    def add_point_manually(event):
        def submit(text):
            try:
                x, y = map(float, text.split(','))
                points.append((x, y))
                update()
            except ValueError:
                print("Input tidak valid. Gunakan format: x,y")

        input_ax = plt.axes([0.1, 0.025, 0.65, 0.04])
        text_box = TextBox(input_ax, 'Masukkan koordinat (x,y): ')
        text_box.on_submit(submit)

    def reset(event):
        points.clear()
        update()

    def done(event):
        plt.close()

    # Button setup
    add_ax = plt.axes([0.7, 0.1, 0.2, 0.04])
    reset_ax = plt.axes([0.7, 0.025, 0.1, 0.04])
    done_ax = plt.axes([0.85, 0.025, 0.1, 0.04])

    add_button = Button(add_ax, 'Add Point', color='lightgoldenrodyellow')
    reset_button = Button(reset_ax, 'Reset', color='lightgoldenrodyellow')
    done_button = Button(done_ax, 'Done', color='lightgreen')

    add_button.on_clicked(add_point_manually)
    reset_button.on_clicked(reset)
    done_button.on_clicked(done)

    fig.canvas.mpl_connect('button_press_event', on_click)
    
    plt.show()
    return points

# Update main section
if __name__ == "__main__":
    points_kubik = []
    while True:
        print("\nMenu Plotting Kurva Bezier:")
        print("1. Input Titik (Plot Titik Manual)")
        print("2. Tampilkan Plot Bezier Statis")
        print("3. Tampilkan Plot Bezier Interaktif")
        print("4. Plot Titik Manual")
        print("5. Keluar")
        
        choice = input("Pilih opsi (1-4): ")
        
        if choice == '1':
            points_kubik = []
            num_points = int(input("Masukan kordinat (minimum 4): "))
            if num_points < 4:
                print("Error: koerdinat harus 4 titik!")
                continue
            for i in range(num_points):
                point = input(f"Masukan kordinat ke {i+1} (format: x,y): ")
                try:
                    x, y = map(float, point.split(','))
                    points_kubik.append((x, y))
                except ValueError:
                    print("Invalid input. Use format: x,y")
                    points_kubik = []
                    break
            if len(points_kubik) < 4:
                print("Error: Perlu >= 4 point!")
                points_kubik = []
                
        elif choice == '2':
            if not points_kubik:
                print("Masukan kordinata terlebih dahulu (Option 1)")
                continue
            delta_t = 0.01
            bzr_kubik = bzr.kubik(delta_t, points_kubik)
            plot_bzier(bzr_kubik)
            
        elif choice == '3':
            if not points_kubik:
                print("Masukan kordinata terlebih dahulu (Option 1)")
                continue
            interactive_plot(points_kubik)
            
        elif choice == '4':
            points = manual_point_plot()
            interactive_plot(points)
        
        elif choice == '5':
            print("Exiting program...")
            break
            
        else:
            print("Invalid option! Please try again.")
