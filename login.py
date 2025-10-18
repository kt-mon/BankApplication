import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import data
import subprocess
import sys

def login():
    login_name = username_var.get()
    login_password = password_var.get()

    for user in data.users:
        if user["name"] == login_name and user["password"] == login_password:
            data.current_user = user
            result_label.configure(text="Login Successful", style="Success.TLabel")
            window.after(2000, lambda: subprocess.Popen([sys.executable, "main_app.py", user["name"]]))
            window.after(2100, window.destroy)
            return
            
    result_label.configure(text="Invalid username or password", style="Error.TLabel")
    username_var.set("")
    password_var.set("")

window = tk.Tk()
window.title("KU+ Login Page")
window.resizable(False, False)
window.configure(bg="#FFFFFF")

style = ttk.Style()
style.theme_use('clam')

k_green = "#00A950"
dark_text = "#333333"
light_text = "#FFFFFF"
bg_white = "#FFFFFF"

style.configure("TFrame", background=bg_white)
style.configure("TLabel", background=bg_white, foreground=dark_text, font=("Helvetica", 12))
style.configure("Header.TLabel", font=("Helvetica", 18, "bold"))
style.configure("Field.TLabel", font=("Helvetica", 11))
style.configure("Success.TLabel", background=bg_white, foreground=k_green, font=("Helvetica", 12))
style.configure("Error.TLabel", background=bg_white, foreground="red", font=("Helvetica", 12))

style.configure("TEntry",
    font=("Helvetica", 12),
    padding=10,
    fieldbackground=bg_white
)

style.configure("App.TButton",
    background=k_green,
    foreground=light_text,
    font=("Helvetica", 14, "bold"),
    borderwidth=0,
    padding=(20, 15)
)
style.map("App.TButton",
    background=[('active', '#007d3c')]
)

main_frame = ttk.Frame(window, style="TFrame", padding=(30, 30, 30, 30))
main_frame.pack(fill="both", expand=True)

try:
    ku_img_open = Image.open("KU+.png")
    ku_img_open = ku_img_open.resize((80, 80))
    ku_img = ImageTk.PhotoImage(ku_img_open)
    img_label = ttk.Label(main_frame, image=ku_img, style="TFrame")
    img_label.image = ku_img
    img_label.pack(pady=(20, 10))
except Exception:
    pass

title_label = ttk.Label(main_frame, text="Login to your account", style="Header.TLabel")
title_label.pack(pady=(10, 30))

username_var = tk.StringVar()
password_var = tk.StringVar()

username_label = ttk.Label(main_frame, text="Username", style="Field.TLabel")
username_label.pack(anchor="w")
username_entry = ttk.Entry(main_frame, textvariable=username_var)
username_entry.pack(fill="x", pady=(5, 15))

password_label = ttk.Label(main_frame, text="Password", style="Field.TLabel")
password_label.pack(anchor="w")
password_entry = ttk.Entry(main_frame, textvariable=password_var, show="*")
password_entry.pack(fill="x", pady=(5, 15))

result_label = ttk.Label(main_frame, text="", style="TLabel")
result_label.pack(pady=(10, 10))

login_button = ttk.Button(main_frame, text="Login", command=login, style="App.TButton")
login_button.pack(fill="x", pady=20)

username_entry.focus()
window.mainloop()