import customtkinter as ctk
import ctypes
import time
import win32gui
import win32con
from threading import Thread


user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
windowList = []
selected_app = ""

def enum_window_proc(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def update_window_list():
    global windowList

    while True:
        temp = []
        win32gui.EnumWindows(enum_window_proc, temp)

        if( windowList != temp ):
            try:
                panel.after(20, refresh_window_list)
            except:
                exit()

        windowList = temp
        time.sleep(2)

def refresh_window_list():
    global window_list_dropdown, windowList
    windowList_strings = [f"{title[0:54]}" for hwnd, title in windowList] #Dirty truncate to resize drop-down UI
    window_list_dropdown.configure(values = windowList_strings)

def change_appearance_mode_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)

def combo_answer(choice):
    global selected_app 
    selected_app = choice
    print("You selected : ", selected_app)

def make_borderless():
    global selected_app, windowList
    
    hwnd = None
    for win_hwnd, win_title in windowList:
        if win_title.startswith(selected_app):
            hwnd = win_hwnd
            break
    
    if hwnd is None:
        print("Error.")
        return
    
    if hwnd:
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE) & ~(win32con.WS_CAPTION)
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)

        win32gui.MoveWindow(hwnd, 0, 0, screen_width - 1, screen_height - 1, True)
        win32gui.SetWindowPos(hwnd, None, 0, 0, screen_width, screen_height, win32con.SWP_NOMOVE | win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED)
   

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

panel = ctk.CTk()
panel.geometry("400x400+"+ str(int(screen_width/2) - 200) + '+' + str(int(screen_height/2) - 200))
panel.resizable(False, False)
panel.title('NoMoreBorder')


label = ctk.CTkLabel(panel, text="Display Resolution is " + str(screen_width) + 'x' + str(screen_height), font = ("Helvetica", 20))
label.pack(pady=20)

window_list_dropdown = ctk.CTkComboBox(panel, values = ["Select Application"], width = 400, command = combo_answer)
window_list_dropdown.pack(padx=20, pady=(0, 10))

submit_button = ctk.CTkButton(panel, text="Make it Borderless", command = make_borderless)
submit_button.pack(pady=10)

toggle_mode = ctk.CTkLabel(panel, text="Appearance Mode:", anchor="w")
toggle_mode.pack(padx=20, pady=(10, 0))

toggle_mode_options = ctk.CTkOptionMenu(panel, values=[ "System", "Light", "Dark" ], command = change_appearance_mode_event)
toggle_mode_options.pack(padx=20, pady=(10, 0))

Thread(target = update_window_list).start()

panel.attributes('-topmost', True)
panel.mainloop()

