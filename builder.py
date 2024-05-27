import customtkinter as ctk
from customtkinter import filedialog
from backend import build_executable

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('green')

font = ('JetBrains Mono', 10)

window = ctk.CTk()
window.title('python executable')
window.geometry('400x300')
window.iconbitmap('C:\\Users\\retr0\\Documents\\python3\\resources\\1492608046-7-docs-document-file-data-google-suits_83383.ico')

global_var_options = False
global_var_filename = ''

def toggle_options():
    global global_var_options
    if global_var_options:
        global_var_options = False
    else:
        global_var_options = True

def build_options():
    toggle_options()
    if global_var_options:
        options_frame.pack(expand=True, fill='both', padx=5, pady=5)

def get_path():
    global global_var_filename
    global_var_filename = filedialog.askopenfilename()

frame1 = ctk.CTkFrame(window)
frame1.pack(expand=True, fill='both', padx=5, pady=5)

load_app = ctk.CTkButton(frame1, text='Select File', command=get_path)
load_app.pack(pady=20)

build_app = ctk.CTkButton(frame1, text='Build Executable', fg_color='#e63746', hover_color='black')
build_app.pack()

switch = ctk.CTkSwitch(frame1, text='custom build', command=build_options)
switch.pack(pady=5)

subframe = ctk.CTkFrame(frame1)
subframe.pack()

label = ctk.CTkLabel(subframe, text='Toggle custom build for icon, name, and run properties.', font=font, text_color='grey')
label.pack(side='left')

options_frame = ctk.CTkFrame(frame1)

window.mainloop()
