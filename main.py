import tkinter
import sv_ttk
from tkinter import ttk
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

screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)



panel = tkinter.Tk()
panel.geometry("400x400+"+ str(int(screen_width/2) - 200) + '+' + str(int(screen_height/2) - 200))
panel.resizable(False, False)
sv_ttk.set_theme("dark")

label = ttk.Label(panel, text="Display Resolution is " + str(screen_width) + 'x' + str(screen_height))
label.pack(pady=20)

type_field = ttk.Entry(panel)
type_field.pack()

submit_button = ttk.Button(panel, text="Submit", command= None)
submit_button.pack(pady=20)

panel.attributes('-topmost', True)
panel.mainloop()