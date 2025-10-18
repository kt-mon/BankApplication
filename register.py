import tkinter as tk
from tkinter import ttk
import subprocess
import sys

def submit():
    import data
    users = data.users
    name = name_var.get()
    age = age_var.get()
    gender = gender_var.get()
    password = password_var.get()

    for user in users:
        if user["name"] == name:
            result_label.configure(text="This name is already taken", style="Error.TLabel")
            return
    if name == "" or age == "" or gender == "" or password == "":
        result_label.configure(text="All fields are required *", style="Error.TLabel")
        return

    users_data = {
        "name" : name ,
        "age" : age,
        "gender" : gender,
        "password" : password,
        "balance" : 0.0
    }

    users.append(users_data)
    with open("data.py", "w", encoding="utf-8") as f:
        f.write("users = " + str(users))

    result_label.configure(text="Account has been created", style="Success.TLabel")

    name_var.set("")
    age_var.set("")
    gender_var.set("")
    password_var.set("")

    window.after(2000,window.destroy)

window = tk.Tk()
window.title("Register Page")
window.geometry("360x640")
window.resizable(False, False)

k_green = "#00A950"
light_text = "#FFFFFF"
dark_text = "#333333"
bg_white = "#FFFFFF"

window.configure(bg=k_green)

style = ttk.Style()
style.theme_use('clam')

style.configure("TFrame", background=k_green)
style.configure("TLabel", background=k_green, foreground=light_text, font=("Helvetica", 12))
style.configure("Header.TLabel", font=("Helvetica", 18, "bold"))
style.configure("Field.TLabel", font=("Helvetica", 11))
style.configure("Success.TLabel", background=k_green, foreground=light_text, font=("Helvetica", 12, "bold"))
style.configure("Error.TLabel", background=k_green, foreground="yellow", font=("Helvetica", 12, "bold"))

style.configure("TEntry",
    font=("Helvetica", 12),
    padding=10,
    fieldbackground=bg_white,
    foreground=dark_text
)

style.configure("App.TButton",
    background=bg_white,
    foreground=k_green,
    font=("Helvetica", 14, "bold"),
    borderwidth=0,
    padding=(20, 15)
)
style.map("App.TButton",
    background=[('active', '#E0E0E0')]
)

main_frame = ttk.Frame(window, style="TFrame", padding=(30, 30, 30, 30))
main_frame.pack(fill="both", expand=True)

name_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar()
password_var = tk.StringVar()

title_label = ttk.Label(main_frame, text="Create your account", style="Header.TLabel")
title_label.pack(anchor="w", pady=(10, 30))

name_label = ttk.Label(main_frame, text="Name", style="Field.TLabel")
name_label.pack(anchor="w")
name_entry = ttk.Entry(main_frame, textvariable=name_var)
name_entry.pack(fill="x", pady=(5, 15))

age_label = ttk.Label(main_frame, text="Age", style="Field.TLabel")
age_label.pack(anchor="w")
age_entry = ttk.Entry(main_frame, textvariable=age_var)
age_entry.pack(fill="x", pady=(5, 15))

gender_label = ttk.Label(main_frame, text="Gender", style="Field.TLabel")
gender_label.pack(anchor="w")
gender_entry = ttk.Entry(main_frame, textvariable=gender_var)
gender_entry.pack(fill="x", pady=(5, 15))

password_label = ttk.Label(main_frame, text="Password", style="Field.TLabel")
password_label.pack(anchor="w")
password_entry = ttk.Entry(main_frame, textvariable=password_var, show="*")
password_entry.pack(fill="x", pady=(5, 15))

result_label = ttk.Label(main_frame, text="", style="TLabel")
result_label.pack(pady=(10, 10))

submit_button = ttk.Button(main_frame, text="Submit", command=submit, style="App.TButton")
submit_button.pack(fill="x", pady=20)

name_entry.focus()
window.mainloop()