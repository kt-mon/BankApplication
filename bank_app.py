import tkinter as tk
from tkinter import ttk
from PIL import  ImageTk, Image  
import subprocess
import sys

def login():
    subprocess.Popen([sys.executable, "login.py"])
    window.destroy()

def register():
    subprocess.Popen([sys.executable, "register.py"])


window = tk.Tk()
window.title("Bank Application")
window.geometry("300x250")
window.attributes("-topmost",1)
window.resizable(False,False)

logo_img = Image.open("Logo_KU+.png")
logo_img = logo_img.resize((100,100))
logo_img = ImageTk.PhotoImage(logo_img)

title_label = ttk.Label(window, text="KU PLUS",font=("Helvetica", 16 ),foreground="green")
title_label.grid(row=0,column=1 ,pady=10,sticky="N")

img_label = ttk.Label(window, image=logo_img)
img_label.grid(row=1,column=1,sticky="N", pady=10)

login_button = ttk.Button(window, text="Login",width=20,command=login)
login_button.grid(row=2,column=1 ,sticky="N")

register_button = ttk.Button(window, text="Register" , width=20, command=register)
register_button.grid(row=3,column=1, sticky="N")


window.columnconfigure(1, weight=1)
window.mainloop()