import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import data
import sys

try:
    name = sys.argv[1]
except IndexError:
    name = "Dev"

current_user = None
for user in data.users:
    if user["name"] == name:
        current_user = user
        data.current_user = user
        break

if current_user is None:
    current_user = {"name": name, "age": "-", "gender": "-", "balance": 0.0}
    data.users.append(current_user)
    data.current_user = current_user

window = tk.Tk()
window.title("KU+")
window.geometry("360x640")
window.resizable(False, False)
window.configure(bg="#F5F6F7")

style = ttk.Style()
style.theme_use('clam')

k_green = "#00A950"
k_dark = "#006A4E"
dark_text = "#222222"
light_text = "#FFFFFF"
bg_main = "#F5F6F7"

style.configure("App.TFrame", background=bg_main)
style.configure("Card.TFrame", background=bg_main)
style.configure("Header.TLabel", background=bg_main, foreground=k_dark, font=("Segoe UI Semibold", 18, "bold"))
style.configure("Welcome.TLabel", background=bg_main, foreground="#555555", font=("Segoe UI", 13))
style.configure("App.TButton", background=k_green, foreground=light_text, font=("Segoe UI", 14, "bold"), borderwidth=0, padding=(20, 15))
style.map("App.TButton", background=[('active', '#009E60')])
style.configure("BalanceTitle.TLabel", background=bg_main, foreground=k_green, font=("Segoe UI Semibold", 16))
style.configure("BalanceValue.TLabel", background=bg_main, foreground=dark_text, font=("Segoe UI", 14, "bold"))

header_frame = ttk.Frame(window, style="App.TFrame", padding=(20, 30, 20, 10))
header_frame.pack(fill="x")

try:
    ku_img = Image.open("Logo_KUplus.png")
    ku_img = ku_img.resize((70, 70))
    ku_img = ImageTk.PhotoImage(ku_img)
    img_label = ttk.Label(header_frame, image=ku_img, background=bg_main)
    img_label.image = ku_img
    img_label.grid(row=0, column=0, rowspan=2, padx=(0, 15))
except:
    placeholder = ttk.Frame(header_frame, width=70, height=70, style="App.TFrame")
    placeholder.grid(row=0, column=0, rowspan=2, padx=(0, 15))

title_label = ttk.Label(header_frame, text="KU PLUS", style="Header.TLabel")
title_label.grid(row=0, column=1, sticky="w")

welcome_label = ttk.Label(header_frame, text=f"Welcome, {current_user['name']}", style="Welcome.TLabel")
welcome_label.grid(row=1, column=1, sticky="w")

card_frame = ttk.Frame(window, style="Card.TFrame", padding=(30, 25))
card_frame.pack(fill="x", pady=(20, 10), padx=25)
card_frame.configure(relief="ridge", borderwidth=1)

balance_title = ttk.Label(card_frame, text="Account Balance", style="BalanceTitle.TLabel")
balance_title.pack(anchor="w", pady=(0, 5))

balance_value = ttk.Label(card_frame, text=f"฿ {current_user['balance']:,.2f}", style="BalanceValue.TLabel")
balance_value.pack(anchor="w")

def update_balance_label():
    balance_value.config(text=f"฿ {current_user['balance']:,.2f}")

def deposit():
    deposit_window = tk.Toplevel(window)
    deposit_window.title("Deposit Money")
    deposit_window.geometry("360x280")
    deposit_window.configure(bg="#F5F6F7")
    deposit_window.attributes("-topmost", 1)
    deposit_window.resizable(False, False)

    tk.Label(deposit_window, text="Deposit Money", font=("Segoe UI Semibold", 18), fg=k_green, bg="#F5F6F7").pack(pady=(20, 10))

    card = tk.Frame(deposit_window, bg="white", bd=1, relief="ridge")
    card.pack(padx=20, pady=10, fill="both", expand=True)

    tk.Label(card, text=f"Current Balance: ฿ {current_user['balance']:,.2f}", font=("Segoe UI", 13), fg=dark_text, bg="white").pack(anchor="w", padx=15, pady=(15,5))

    tk.Label(card, text="Enter amount to deposit:", font=("Segoe UI", 12), fg=dark_text, bg="white").pack(anchor="w", padx=15, pady=(10,5))

    amount_var = tk.StringVar()
    amount_entry = ttk.Entry(card, textvariable=amount_var, font=("Segoe UI", 12))
    amount_entry.pack(fill="x", padx=15, pady=(0,10))
    amount_entry.focus()

    def confirm_deposit():
        try:
            amount = float(amount_var.get())
            if amount <= 0:
                messagebox.showwarning("Invalid", "Enter a valid amount!")
                return
            current_user['balance'] += amount
            update_balance_label()
            messagebox.showinfo("Success", f"Successfully deposited ฿ {amount:,.2f}")
            deposit_window.destroy()
        except ValueError:
            messagebox.showwarning("Invalid", "Enter a valid number!")

    confirm_btn = tk.Button(card, text="Confirm", font=("Segoe UI", 14, "bold"),
                            bg=k_green, fg=light_text, activebackground="#009E60",
                            activeforeground=light_text, bd=0, padx=20, pady=10,
                            command=confirm_deposit)
    confirm_btn.pack(fill="x", padx=15, pady=(10, 15))

def withdraw():
    withdraw_window = tk.Toplevel(window)
    withdraw_window.title("Withdraw Money")
    withdraw_window.geometry("360x280")
    withdraw_window.configure(bg="#F5F6F7")
    withdraw_window.attributes("-topmost", 1)
    withdraw_window.resizable(False, False)

    tk.Label(withdraw_window, text="Withdraw Money", font=("Segoe UI Semibold", 18), fg=k_green, bg="#F5F6F7").pack(pady=(20, 10))

    card = tk.Frame(withdraw_window, bg="white", bd=1, relief="ridge")
    card.pack(padx=20, pady=10, fill="both", expand=True)

    tk.Label(card, text=f"Current Balance: ฿ {current_user['balance']:,.2f}", font=("Segoe UI", 13), fg=dark_text, bg="white").pack(anchor="w", padx=15, pady=(15,5))

    tk.Label(card, text="Enter amount to withdraw:", font=("Segoe UI", 12), fg=dark_text, bg="white").pack(anchor="w", padx=15, pady=(10,5))

    amount_var = tk.StringVar()
    amount_entry = ttk.Entry(card, textvariable=amount_var, font=("Segoe UI", 12))
    amount_entry.pack(fill="x", padx=15, pady=(0,10))
    amount_entry.focus()

    def confirm_withdraw():
        try:
            amount = float(amount_var.get())
            if amount <= 0:
                messagebox.showwarning("Invalid", "Enter a valid amount!")
                return
            if amount > current_user['balance']:
                messagebox.showerror("Error", "Insufficient balance")
                return
            current_user['balance'] -= amount
            update_balance_label()
            messagebox.showinfo("Success", f"Successfully withdrew ฿ {amount:,.2f}")
            withdraw_window.destroy()
        except ValueError:
            messagebox.showwarning("Invalid", "Enter a valid number!")

    confirm_btn = tk.Button(card, text="Confirm", font=("Segoe UI", 14, "bold"),
                            bg=k_green, fg=light_text, activebackground="#009E60",
                            activeforeground=light_text, bd=0, padx=20, pady=10,
                            command=confirm_withdraw)
    confirm_btn.pack(fill="x", padx=15, pady=(10, 15))

def show_personal_details():
    details_window = tk.Toplevel(window)
    details_window.title(f"{current_user['name']}'s Details")
    details_window.configure(bg="#F5F6F7")
    details_window.attributes("-topmost", 1)
    details_window.resizable(False, False)
    details_window.geometry("360x280")
    
    header_label = tk.Label(details_window, text="Personal Details",
                            font=("Segoe UI Semibold", 18),
                            fg=k_green, bg="#F5F6F7")
    header_label.pack(pady=(20, 10))

    card = tk.Frame(details_window, bg="white", bd=1, relief="solid")
    card.pack(padx=20, pady=10, fill="both", expand=True)

    tk.Label(card, text=f"Name: {current_user['name']}", font=("Segoe UI", 13), fg=dark_text, bg="white", anchor="w").pack(fill="x", padx=15, pady=(15,5))
    tk.Label(card, text=f"Age: {current_user.get('age','-')}", font=("Segoe UI", 13), fg=dark_text, bg="white", anchor="w").pack(fill="x", padx=15, pady=5)
    tk.Label(card, text=f"Gender: {current_user.get('gender','-')}", font=("Segoe UI", 13), fg=dark_text, bg="white", anchor="w").pack(fill="x", padx=15, pady=(5,15))

    details_window.transient(window)
    details_window.grab_set()
    window.wait_window(details_window)

button_frame = ttk.Frame(window, style="App.TFrame", padding=(30, 20))
button_frame.pack(fill="both", expand=True)

personal_btn = ttk.Button(button_frame, text="Personal Details", style="App.TButton", command=show_personal_details)
personal_btn.pack(fill="x", pady=10)

deposit_btn = ttk.Button(button_frame, text="Deposit", style="App.TButton", command=deposit)
deposit_btn.pack(fill="x", pady=10)

withdraw_btn = ttk.Button(button_frame, text="Withdraw", style="App.TButton", command=withdraw)
withdraw_btn.pack(fill="x", pady=10)

footer_label = ttk.Label(window, text="KUBank", background=bg_main, foreground="#777777", font=("Segoe UI", 9))
footer_label.pack(side="bottom", pady=10)

window.mainloop()
