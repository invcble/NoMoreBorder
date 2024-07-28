import customtkinter as ctk
import ctypes, sys
import time
import win32gui
import win32con
import json
import threading
import winreg as reg
from PIL import Image, ImageDraw
from pystray import Icon, MenuItem, Menu
from threading import Thread
from screeninfo import get_monitors

user32 = ctypes.windll.user32
# user32.SetProcessDPIAware()
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
Geometry = "400x300+"+ str(int(screen_width/2) - 200) + '+' + str(int(screen_height/2) - 200)
windowList = []
saveList = {}
selected_app = "0"
monitors = {}
selected_monitor = None
tray_icon = None

# Get monitor info from screeninfo
for index, m in enumerate(get_monitors()):
    name = f"Display {str(index + 1)}" 
    if(m.is_primary):
        name += " (Primary)"
        selected_monitor = name
    monitors[name] = m

resolution_options = {
    "Use Display Resolution": None,
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
selected_resolution = "Use Display Resolution"

def enum_window_proc(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def update_window_list():
    global windowList, saveList, selected_app, selected_resolution, selected_monitor

    while True:
        temp = []
        win32gui.EnumWindows(enum_window_proc, temp)

        temp_titles = [title for hwnd, title in temp]
        for save_item in saveList:
            for temp_title in temp_titles:
                if temp_title.startswith(save_item):
                    # Use saved settings if they exist
                    make_borderless(save_item, saveList[save_item]["resolution"], saveList[save_item]["monitor"], write_needed=False) 

        if( windowList != temp ):
            try:
                panel.after(20, refresh_window_list)
            except:
                exit()

        windowList = temp
        time.sleep(2)

def refresh_window_list():
    global window_list_dropdown, windowList
    # Dirty truncate to resize drop-down UI
    windowList_strings = [f"{title[0:50]}" for hwnd, title in windowList]
    window_list_dropdown.configure(values = windowList_strings)

    
def load_settings():
    try:
        with open("settings.json", "r") as f:
            settings = json.load(f)
            if isinstance(settings["apps"], list):
                settings["apps"] = {app:{
                    "monitor": "Display 1 (Primary)",
                    "resolution": "Use Display Resolution"
                    } for app in settings["apps"]}
                save_settings(settings)
            if "start_with_windows" not in settings:
                settings["start_with_windows"] = False
            return settings
    except:
        return {"theme": "System", "apps": {}, "start_with_windows": False}

def save_settings(settings):
    try:
        with open("settings.json", "w") as f:
            json.dump(settings, f, indent=4)
    except:
        pass

def change_start_with_windows_event():
    global check_box
    settings = load_settings()
    start_with_windows = check_box.get() == 1
    settings["start_with_windows"] = start_with_windows
    set_startup(start_with_windows)
    save_settings(settings)

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
    selected_resolution = choice

def combo_answer_display(choice):
    global selected_monitor
    selected_monitor = choice
    label.configure(text="Display Resolution is " + str(monitors[choice].width) + 'x' + str(monitors[choice].height))

def make_borderless(app_name = None, resolution_string = None, monitor_name = None, write_needed = True):
    global selected_app, windowList, saveList
    
    app_name = app_name or selected_app
    resolution_string = resolution_string or selected_resolution
    monitor_name = monitor_name or selected_monitor
    
    hwnd = None
    for win_hwnd, win_title in windowList:
        if win_title.startswith(app_name):
            hwnd = win_hwnd
            break
    
    if hwnd is None:
        return

    if write_needed:
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        pre_win_height = bottom - top
        pre_win_width = right - left

    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE) & ~(win32con.WS_CAPTION) & ~(win32con.WS_THICKFRAME)

    style 
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)

    if(resolution_string == "Use Display Resolution"):
        target_resolution = (monitors[monitor_name].width, monitors[monitor_name].height)
    else:
        target_resolution = resolution_options[resolution_string]

    # Center on screen
    location_x = monitors[monitor_name].x + monitors[monitor_name].width//2 - (target_resolution[0]//2)
    location_y = monitors[monitor_name].y + monitors[monitor_name].height//2 - (target_resolution[1]//2)

    # Move window
    win32gui.MoveWindow(hwnd, location_x, location_y, target_resolution[0], target_resolution[1], True)
    win32gui.SetWindowPos(hwnd, None, location_x, location_y, target_resolution[0], target_resolution[1], win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED)

    if write_needed:
        saveList[app_name] = {}
        saveList[app_name]["monitor"] = monitor_name
        saveList[app_name]["resolution"] = resolution_string
        saveList[app_name]["pre_win_height"] = pre_win_height
        saveList[app_name]["pre_win_width"] = pre_win_width        
        update_apps(saveList)
    else:
        # Always update saveList in case the selected resolution or monitor has changed
        saveList[app_name]["monitor"] = monitor_name
        saveList[app_name]["resolution"] = resolution_string
        update_apps(saveList)

def restore_window():
    global selected_app, windowList, saveList

    app_name = selected_app
    pre_win_height = saveList[app_name]["pre_win_height"]
    pre_win_width = saveList[app_name]["pre_win_width"]  
    
    hwnd = None
    for win_hwnd, win_title in windowList:
        if win_title.startswith(selected_app):
            hwnd = win_hwnd
            break
    
    if hwnd is None:
        return
    
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE) | win32con.WS_CAPTION | win32con.WS_SYSMENU | win32con.WS_MINIMIZEBOX | win32con.WS_MAXIMIZEBOX | win32con.WS_THICKFRAME
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)
    
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 350, 200, pre_win_width, pre_win_height, win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED)
    
    if selected_app in saveList:
        saveList.pop(selected_app)
        update_apps(saveList)

def on_quit(icon, item):
    icon.stop()
    panel.after(0, panel.quit)

def on_show(icon, item):
    global tray_icon
    icon.stop()
    
    panel.geometry(Geometry)
    
    def do1():
        panel.attributes("-alpha", 0)   
    panel.after(10, do1())
    
    panel.deiconify()
    panel.update_idletasks()
    panel.update()
    
    def do2():
        panel.attributes("-alpha", 1)   
    panel.after(1000, do2())
    
    tray_icon = None

def create_custom_icon():
    image = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    draw.rectangle([0, 0, 64, 64], fill=(0, 156,255,255))
    draw.rectangle([16, 16, 64, 48], fill=(0, 0, 0, 0))
    draw.rectangle([48, 16, 64, 48], fill=(0, 98,177,255))
    return image

def minimize_to_tray(event=None):
    global tray_icon
    panel.withdraw()
    if tray_icon is None:
        menu = Menu(
            MenuItem('Show', on_show),
            MenuItem('Quit', on_quit)
        )
        tray_icon = Icon("NoMoreBorder", create_custom_icon(), "NoMoreBorder", menu)
        threading.Thread(target=tray_icon.run, daemon=True).start()

def set_startup(startup):
    s_name = "NoMoreBorder"
    address = sys.executable
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"

    open_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_ALL_ACCESS)
    
    if startup:
        reg.SetValueEx(open_key, s_name, 0, reg.REG_SZ, address)
    else:
        try:
            reg.DeleteValue(open_key, s_name)
        except FileNotFoundError:
            pass
    reg.CloseKey(open_key)

current_settings = load_settings()
saveList = current_settings["apps"]
ctk.set_appearance_mode(current_settings["theme"])
ctk.set_default_color_theme("blue")  # Themes: "blue" / "green" / "dark-blue"


panel = ctk.CTk()
panel.geometry(Geometry)
panel.resizable(False, False)
panel.title('NoMoreBorder')

if current_settings["start_with_windows"] == True:
    minimize_to_tray()

label = ctk.CTkLabel(panel, text="Display Resolution is " + str(monitors[selected_monitor].width) + 'x' + str(monitors[selected_monitor].height), font = ("Helvetica", 20))
label.pack(pady=20)

window_list_dropdown = ctk.CTkComboBox(panel, values = ["Select Application"], width = 400, command = combo_answer)
window_list_dropdown.pack(padx=20, pady=(0, 10))

monitor_frame = ctk.CTkFrame(panel, fg_color = "transparent")
monitor_frame.pack(pady=10)

monitor_dropdown = ctk.CTkComboBox(monitor_frame, values = list(monitors.keys()), width = 175, command = combo_answer_display)
# Main display isn't always Display 1, so set whatever the system default is
monitor_dropdown.set(selected_monitor)
monitor_dropdown.grid(row=0, column=0, padx=(20, 5), pady=(0, 10))

resolution_dropdown = ctk.CTkComboBox(monitor_frame, values = list(resolution_options.keys()), width = 175, command = combo_answer_resolution)
resolution_dropdown.grid(row=0, column=1, padx=(5, 20), pady=(0, 10))

buttons_frame = ctk.CTkFrame(panel, fg_color = "transparent")
buttons_frame.pack(pady=5)

submit_button = ctk.CTkButton(buttons_frame, text="Make it Borderless", command = make_borderless, height=35)
submit_button.grid(row=0, column=0, padx=5)

undo_button = ctk.CTkButton(buttons_frame, text="Undo Lmao!", command = restore_window, height=35)
undo_button.grid(row=0, column=1, padx=5)

check_box = ctk.CTkCheckBox(panel, text='Start with Windows', command=change_start_with_windows_event)
check_box.pack(padx=20, pady=(24, 0))
check_box.select() if current_settings["start_with_windows"] else check_box.deselect()

buttons_frame2 = ctk.CTkFrame(panel, fg_color = "transparent")
buttons_frame2.pack(pady=0)

toggle_mode = ctk.CTkLabel(buttons_frame2, text="Appearance Mode:", anchor="w")
toggle_mode.grid(row=1, column=0, padx=5, pady=5)

toggle_mode_options = ctk.CTkOptionMenu(buttons_frame2, values=[ "System", "Light", "Dark" ], command = change_appearance_mode_event, width=100, height=22)
toggle_mode_options.grid(row=1, column=1, padx=10, pady=5)
toggle_mode_options.set(current_settings["theme"])

Thread(target = update_window_list).start()

panel.bind('<Unmap>', minimize_to_tray)
# panel.attributes('-topmost', True)
panel.mainloop()

if tray_icon is not None:
    tray_icon.stop()