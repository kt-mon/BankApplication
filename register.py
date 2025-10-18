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
            result_label.configure(text="This name is already have", foreground="orange")
            return
    if name == "" or age == "" or gender == "" or password == "":
        result_label.configure(text="All fields requried *", foreground="red")
        return

    users_data = {
        "name" : name ,
        "age" : age,
        "gender" : gender,
        "password" : password
    }

    users.append(users_data)
    with open("data.py", "w", encoding="utf-8") as f:
        f.write("users = " + str(users))

    result_label.configure(text="Account has been created", foreground="green")

    name_var.set("")
    age_var.set("")
    gender_var.set("")
    password_var.set("")

    window.after(2000,window.destroy)
    

window = tk.Tk()
window.title("Register Page")
window.attributes("-topmost",1)
window.resizable(False,False)

name_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar()
password_var = tk.StringVar()

detail_label = ttk.Label(window, text="Plese enter your detail to register", font=("Helvetica",10))
detail_label.grid(row=0, sticky="W" )

name_label = ttk.Label(window, text="Name", font=("Helvetica",10))
name_label.grid(row=1, sticky="W" ,pady=10)
name_entry = ttk.Entry(window,textvariable=name_var)
name_entry.grid(row=1, column=0, padx=50)

age_label = ttk.Label(window, text="Age", font=("Helvetica",10))
age_label.grid(row=2, sticky="W" ,pady = 10)
age_entry = ttk.Entry(window,textvariable=age_var)
age_entry.grid(row=2, column=0, padx=50)

gender_label = ttk.Label(window, text="Gender", font=("Helvetica",10))
gender_label.grid(row=3, sticky="W", pady=10 )
gender_entry = ttk.Entry(window,textvariable=gender_var)
gender_entry.grid(row=3, column=0, padx=50)

password_label = ttk.Label(window, text="Password", font=("Helvetica",10))
password_label.grid(row=4, sticky="W",pady=10 )
password_entry = ttk.Entry(window,textvariable=password_var,show="*")
password_entry.grid(row=4, column=0, padx=70)

submit_button = ttk.Button(window, text="Submit", command=submit)
submit_button.grid(row=5, column=0, padx=65)

result_label = ttk.Label(window, text="", font=("Helvetica", 10))
result_label.grid(row=6,column=0, padx=50)

name_entry.focus()
window.mainloop()