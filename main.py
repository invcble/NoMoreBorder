import customtkinter as ctk
import ctypes
import time
import win32gui
import win32con
import json
from threading import Thread


user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
windowList = []
saveList = []
selected_app = "0"
temp_win_height = 1080
temp_win_width = 1920

resolition_options = {
    "Use Display Resolution": (screen_width, screen_height),
    "3840x2160": (3840, 2160),
    "3440x1440": (3440, 1440),
    "2560x1600": (2560, 1600),
    "2560x1440": (2560, 1440),
    "2560x1600": (2560, 1600),
    "2560x1080": (2560, 1080),
    "1920x1200": (1920, 1200),
    "1920x1080": (1920, 1080),
    "1680x1050": (1680, 1050),
    "1600x900": (1600, 900),
    "1440x900": (1440, 900),
    "1366x768": (1366, 768),
    "1280x720": (1280, 720),
    "1280x1024": (1280, 1024),
    "1024x768": (1024, 768),
    "800x600": (800, 600),
    "640x480": (640, 480),
}
selected_resolution = resolition_options["Use Display Resolution"]

def enum_window_proc(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def update_window_list():
    global windowList, saveList, selected_app

    while True:
        temp = []
        win32gui.EnumWindows(enum_window_proc, temp)

        temp_titles = [title for hwnd, title in temp]
        for save_item in saveList:
            for temp_title in temp_titles:
                if temp_title.startswith(save_item):
                    Temp = selected_app
                    selected_app = save_item
                    make_borderless(check = 1)  #Check 1 to skip loading temp resolution 
                    selected_app = Temp

        if( windowList != temp ):
            try:
                panel.after(20, refresh_window_list)
            except:
                exit()

        windowList = temp
        time.sleep(2)

def refresh_window_list():
    global window_list_dropdown, windowList
    windowList_strings = [f"{title[0:50]}" for hwnd, title in windowList] #Dirty truncate to resize drop-down UI
    window_list_dropdown.configure(values = windowList_strings)

    
def load_settings():
    try:
        with open("settings.json", "r") as f:
            return json.load(f)
    except:
        return {"theme": "System", "apps": []}

def save_settings(settings):
    try:
        with open("settings.json", "w") as f:
            json.dump(settings, f, indent=4)
    except:
        pass

def update_theme(new_theme):
    settings = load_settings()
    settings["theme"] = new_theme
    save_settings(settings)

def update_apps(new_apps):
    settings = load_settings()
    settings["apps"] = new_apps
    save_settings(settings)

def change_appearance_mode_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)
    update_theme(new_appearance_mode)

def combo_answer(choice):
    global selected_app 
    selected_app = choice

def combo_answer_resolution(choice):
    global selected_resolution 
    selected_resolution = resolition_options[choice]

def make_borderless(check = None):
    global selected_app, windowList, saveList, temp_win_height, temp_win_width
    
    hwnd = None
    for win_hwnd, win_title in windowList:
        if win_title.startswith(selected_app):
            hwnd = win_hwnd
            break
    
    if hwnd is None:
        return

    if check == None:
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        temp_win_height = bottom - top
        temp_win_width = right - left

    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE) & ~(win32con.WS_CAPTION) & ~(win32con.WS_THICKFRAME)

    style 
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)

    # Center on screen
    location_x = screen_width//2 - (selected_resolution[0]//2)
    location_y = screen_height//2 - (selected_resolution[1]//2)

    win32gui.MoveWindow(hwnd, location_x, location_y, selected_resolution[0], selected_resolution[1], True)
    win32gui.SetWindowPos(hwnd, None, location_x, location_y, selected_resolution[0], selected_resolution[1], win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED)

    if selected_app not in saveList:
        saveList.append(selected_app)
        update_apps(saveList)

def restore_window():
    global selected_app, windowList, temp_win_height, temp_win_width
    
    hwnd = None
    for win_hwnd, win_title in windowList:
        if win_title.startswith(selected_app):
            hwnd = win_hwnd
            break
    
    if hwnd is None:
        return
    
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE) | win32con.WS_CAPTION | win32con.WS_SYSMENU | win32con.WS_MINIMIZEBOX | win32con.WS_MAXIMIZEBOX | win32con.WS_THICKFRAME
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)
    
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 350, 200, temp_win_width, temp_win_height, win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED)
    
    if selected_app in saveList:
        saveList.remove(selected_app)
        update_apps(saveList)

current_settings = load_settings()
saveList = current_settings["apps"]
ctk.set_appearance_mode(current_settings["theme"])
ctk.set_default_color_theme("blue")  # Themes: "blue" / "green" / "dark-blue"

panel = ctk.CTk()
panel.geometry("400x300+"+ str(int(screen_width/2) - 200) + '+' + str(int(screen_height/2) - 200))
panel.resizable(False, False)
panel.title('NoMoreBorder')


label = ctk.CTkLabel(panel, text="Display Resolution is " + str(screen_width) + 'x' + str(screen_height), font = ("Helvetica", 20))
label.pack(pady=20)

window_list_dropdown = ctk.CTkComboBox(panel, values = ["Select Application"], width = 400, command = combo_answer)
window_list_dropdown.pack(padx=20, pady=(0, 10))

resolution_dropdown = ctk.CTkComboBox(panel, values = list(resolition_options.keys()), width = 400, command = combo_answer_resolution)
resolution_dropdown.pack(padx=20, pady=(0, 10))

buttons_frame = ctk.CTkFrame(panel, fg_color = "transparent")
buttons_frame.pack(pady=10)

submit_button = ctk.CTkButton(buttons_frame, text="Make it Borderless", command = make_borderless)
submit_button.grid(row=0, column=0, padx=5)

undo_button = ctk.CTkButton(buttons_frame, text="Undo Lmao!", command = restore_window)
undo_button.grid(row=0, column=1, padx=5)

toggle_mode = ctk.CTkLabel(panel, text="Appearance Mode:", anchor="w")
toggle_mode.pack(padx=20, pady=(10, 0))

toggle_mode_options = ctk.CTkOptionMenu(panel, values=[ "System", "Light", "Dark" ], command = change_appearance_mode_event)
toggle_mode_options.pack(padx=20, pady=(10, 0))
toggle_mode_options.set(current_settings["theme"])

Thread(target = update_window_list).start()

# panel.attributes('-topmost', True)
panel.mainloop()

