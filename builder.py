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
global_var_name = ''
global_var_windowed = False
global_var_icon = False

def toggle_options():
    global global_var_options
    global_var_options = False if global_var_options else True

def toggle_windowed():
    global global_var_windowed
    global_var_windowed = False if global_var_windowed else True

def build_options():
    toggle_options()
    if global_var_options:
        options_frame.pack(expand=True, fill='both', padx=5, pady=5)

def askfileicon():
    global global_var_icon
    global_var_icon = filedialog.askopenfilename()

def get_path():
    global global_var_filename
    global_var_filename = filedialog.askopenfilename()

def init_build():
    build_app.configure(text="Building...")
    build_executable(global_var_name, True, global_var_windowed, global_var_icon)

frame1 = ctk.CTkFrame(window)
frame1.pack(expand=True, fill='both', padx=5, pady=5)

load_app = ctk.CTkButton(frame1, text='Select File', command=get_path)
load_app.pack(pady=20)

build_app = ctk.CTkButton(frame1, text='Build Executable', fg_color='#e63746', hover_color='black', command=init_build)
build_app.pack()

switch = ctk.CTkSwitch(frame1, text='custom build', command=build_options)
switch.pack(pady=5)

subframe = ctk.CTkFrame(frame1)
subframe.pack()

label = ctk.CTkLabel(subframe, text='Toggle custom build for icon, name, and run properties.', font=font, text_color='grey')
label.pack(side='left')

options_frame = ctk.CTkFrame(frame1)

entry = ctk.CTkEntry(options_frame, textvariable=global_var_name, placeholder_text="name of application")
entry.pack(padx=5, pady=5, fill='x')

windowed = ctk.CTkSwitch(options_frame, text="Windowed", command=toggle_windowed)
windowed.pack(padx=5, pady=5, fill='x')

select_path = ctk.CTkButton(options_frame, text="Select Icon", command=askfileicon)
select_path.pack()

window.mainloop()
