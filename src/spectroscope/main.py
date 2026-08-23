from nicegui import ui
import numpy as np

ui.label('Hello NiceGUI!')

# Create a label with initial random numbers and save a reference to it
random_label = ui.label(f"Random numbers are:\n{np.random.normal(1, 10, size=(3, 3))}")

def refresh_data():
    # Generate new random numbers and update the label's text
    new_data = np.random.normal(1, 10, size=(3, 3))
    random_label.text = f"Random numbers are:\n{new_data}"

# Add a button that calls the refresh function on click
ui.button('Refresh Data', on_click=refresh_data)

ui.run(port=8081, show=False, reload=False, title="CBK Spectrometer")