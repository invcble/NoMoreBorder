import customtkinter as ctk
import darkdetect
import ctypes


user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)



panel = ctk.CTk()
panel.geometry("400x400+"+ str(int(screen_width/2) - 200) + '+' + str(int(screen_height/2) - 200))
panel.resizable(False, False)
panel.title('NoMoreBorder')



label = ctk.CTkLabel(panel, text="Display Resolution is " + str(screen_width) + 'x' + str(screen_height))
label.pack(pady=20)

type_field = ctk.CTkEntry(panel)
type_field.pack()

submit_button = ctk.CTkButton(panel, text="Submit", command= None)
submit_button.pack(pady=20)

panel.attributes('-topmost', True)
panel.mainloop()