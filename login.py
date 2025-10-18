import tkinter as tk
from tkinter import ttk
import data
import subprocess
import sys

def login():
    login_name = username_var.get()
    login_password = password_var.get()

    for user in data.users:
        if user["name"] == login_name and user["password"] == login_password:
            result_label.configure(text="Login sucessful", foreground="Green")
            window.after(3000,lambda : subprocess.Popen([sys.executable, "main_app.py"]))
            window.after(3100,window.destroy)
            return
        
        result_label.configure(text="Invalid username or password", foreground="red")
        username_var.set("")
        password_var.set("")


window = tk.Tk()
window.title("KU+ Login Page")
window.attributes("-topmost",1)
window.resizable(False,False)

username_var = tk.StringVar()
password_var = tk.StringVar()

title_label = ttk.Label(window, text="Login to your account", font=("Helvetica",12))
title_label.grid(row=0, sticky="N", pady=10)

username_label = ttk.Label(window, text="Username", font=("Helvetica",12))
username_label.grid(row=1,sticky="W")
username_entry = ttk.Entry(window, textvariable=username_var)
username_entry.grid(row=1, column=0, padx=100, pady=5)

password_labbel = ttk.Label(window, text="Password", font=("Helvetica",12))
password_labbel.grid(row=2, sticky="W")
password_entry = ttk.Entry(window, textvariable=password_var,show="*")
password_entry.grid(row=2, column=0, padx=100,pady=5)

login_button = ttk.Button(window, text="Login",command=login)
login_button.grid(row=3, sticky="W", padx=120, pady=5)

result_label = ttk.Label(window, text="", font=("Helvetica",12))
result_label.grid(row=4,column=0 , sticky="N", pady=10)

username_entry.focus()
window.mainloop()   