from nicegui import ui
import numpy as np
import multiprocessing
import matplotlib.pyplot as plt


def app_main():
    ui.label('Matplotlib Test')

    # Generate 1000 points so the histogram actually looks like a normal distribution
    initial_data = np.random.normal(1, 10, size=1000)

    # Text label for basic stats
    stats_label = ui.label(f"Mean: {np.mean(initial_data):.2f} | Std: {np.std(initial_data):.2f}")

    # 1. Create the plot container
    with ui.pyplot(figsize=(6, 4)) as plot:
        plt.hist(initial_data, bins=30, color='blue', alpha=0.7, edgecolor='black')
        plt.title("Normal Distribution")
        plt.xlabel("Value")
        plt.ylabel("Frequency")

    def refresh_data():
        # Generate new random data
        new_data = np.random.normal(1, 10, size=1000)
        stats_label.text = f"Mean: {np.mean(new_data):.2f} | Std: {np.std(new_data):.2f}"

        # 2. Update the plot container
        with plot:
            plt.clf()  # Clear the old histogram
            plt.hist(new_data, bins=30, color='green', alpha=0.7, edgecolor='black')
            plt.title("Normal Distribution (Refreshed)")
            plt.xlabel("Value")
            plt.ylabel("Frequency")

        # 3. Push the updated image to the UI
        plot.update()

    ui.button('Refresh Data', on_click=refresh_data)
if __name__ in {"__main__", "__mp_main__"}:
    # Crucial to prevent fork-bombing in Windows PyInstaller builds
    multiprocessing.freeze_support()

    # native=True opens it as a standalone desktop window rather than a browser tab
    # reload=False is mandatory for packaged applications
    ui.run(app_main, port=8081, reload=False, native=True, title="Carl/SPEX Spectrometer")