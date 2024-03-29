import customtkinter as ctk
import ctypes
import time
import win32gui
from threading import Thread
import random


user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
windowList = []



def enum_window_proc(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def update_window_list():
    global windowList

    while True:
        temp = []
        # win32gui.EnumWindows(enum_window_proc, temp)
        temp = [str(random.randint(100, 999)) for _ in range(3)]

        if( windowList != temp ):
            panel.after(20, refresh_window_list)

        windowList = temp
        time.sleep(2)

def refresh_window_list():
    global window_list_dropdown, windowList
    

    window_list_dropdown.configure(values = windowList)

    # panel.after(2000, refresh_window_list)
   

panel = ctk.CTk()
panel.geometry("400x400+"+ str(int(screen_width/2) - 200) + '+' + str(int(screen_height/2) - 200))
panel.resizable(False, False)
panel.title('NoMoreBorder')


label = ctk.CTkLabel(panel, text="Display Resolution is " + str(screen_width) + 'x' + str(screen_height))
label.pack(pady=20)

type_field = ctk.CTkEntry(panel)
type_field.pack()

submit_button = ctk.CTkButton(panel, text="Submit", command = None)
submit_button.pack(pady=20)

window_list_dropdown = ctk.CTkOptionMenu(panel, dynamic_resizing = False, values = ["Select Application"])
window_list_dropdown.pack(padx=20, pady=(20, 10))


# panel.after(2000, refresh_window_list)
Thread(target = update_window_list).start()


#######
#######

panel.attributes('-topmost', True)
panel.mainloop()


# while True:
#     windowList = []
#     time.sleep(2)
#     win32gui.EnumWindows(enum_window_proc, windowList)


#     for hwnd, title in windowList:
#         print(f"HWND: {hwnd}, Title: {title}")
    
#     print("####################################")