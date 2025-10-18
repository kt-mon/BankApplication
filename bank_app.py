import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess
import sys

def login():
    subprocess.Popen([sys.executable, "login.py"])
    window.destroy()

def register():
    subprocess.Popen([sys.executable, "register.py"])

window = tk.Tk()
window.title("KU PLUS Bank Application")
window.geometry("340x460")
window.resizable(False, False)
window.configure(bg="#006A4E")

try:
    logo_img = Image.open("Logo_KUplus.png")
    logo_img = logo_img.resize((120, 120))
    logo_img = ImageTk.PhotoImage(logo_img)
except:
    logo_img = None

style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel",
                background="#006A4E",
                foreground="white",
                font=("Segoe UI", 12, "bold"))

style.configure("TButton",
                font=("Segoe UI", 11, "bold"),
                foreground="white",
                background="#00A86B",
                borderwidth=0,
                padding=10)

style.map("TButton",
          background=[("active", "#00C77B"), ("pressed", "#009E60")])

if logo_img:
    img_label = ttk.Label(window, image=logo_img, background="#006A4E")
    img_label.pack(pady=(40, 10))

title_label = ttk.Label(window, text="KU PLUS", font=("Segoe UI Semibold", 20, "bold"))
title_label.pack(pady=(0, 20))

button_frame = tk.Frame(window, bg="#006A4E")
button_frame.pack(pady=10)

login_button = ttk.Button(button_frame, text="เข้าสู่ระบบ", width=20, command=login)
login_button.pack(pady=10)

register_button = ttk.Button(button_frame, text="สมัครสมาชิก", width=20, command=register)
register_button.pack(pady=10)

footer_label = ttk.Label(window,
                         text="KUBank",
                         font=("Segoe UI", 9),
                         foreground="#DFFFE2",
                         background="#006A4E")
footer_label.pack(side="bottom", pady=15)

window.mainloop()
