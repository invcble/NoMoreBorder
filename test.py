import tkinter as tk
from PIL import Image
from pystray import Icon, MenuItem, Menu
import threading

# Create the main window
panel = tk.Tk()
panel.geometry("400x300")
panel.title("NoMoreBorder")

# Global variable to hold the tray icon
tray_icon = None

# Define functions for system tray actions
def on_quit(icon, item):
    icon.stop()
    panel.after(0, panel.quit)

def on_show(icon, item):
    global tray_icon
    icon.stop()
    panel.after(0, lambda: (panel.deiconify(), panel.after(5000, finalize_show)))
    tray_icon = None

# Function to finalize showing the window after a delay
def finalize_show():
    panel.update_idletasks()  # Render the UI first
    panel.deiconify()  # Now make the window visible

# Function to minimize to tray
def minimize_to_tray(event=None):
    global tray_icon
    panel.withdraw()
    if tray_icon is None:
        menu = Menu(
            MenuItem('Show', on_show),
            MenuItem('Quit', on_quit)
        )
        tray_icon = Icon("NoMoreBorder", Image.open("icon.png"), "NoMoreBorder", menu)
        threading.Thread(target=tray_icon.run, daemon=True).start()

# Bind the minimize event to minimize to tray
panel.bind('<Unmap>', minimize_to_tray)

# Example UI elements
button1 = tk.Button(panel, text="Button 1")
button1.pack(pady=10)
button2 = tk.Button(panel, text="Button 2")
button2.pack(pady=10)

# Run the main loop
panel.mainloop()

# Ensure tray icon is stopped on exit
if tray_icon is not None:
    tray_icon.stop()
