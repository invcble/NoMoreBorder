import tkinter as tk
from tkinter import messagebox
import xmlrpc.client
import time
import subprocess
from threading import Thread
import sys
import os
import ctypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

screen_width = str(user32.GetSystemMetrics(0))
screen_height = str(user32.GetSystemMetrics(1))



panel = tk.Tk()
panel.geometry("400x400")
panel.resizable(False, False)
panel.title("Control Panel")

label = tk.Label(panel, text="Welcome to NoMoreBorder\n Display Resolution is " + screen_width + 'x' + screen_height)
label.pack(pady=20)

type_field = tk.Entry(panel)
type_field.pack()

submit_button = tk.Button(panel, text="Submit", command= None)
submit_button.pack(pady=20)

panel.attributes('-topmost', True)
panel.mainloop()