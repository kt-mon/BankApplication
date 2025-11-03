import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image


#-----Data-----
GLOBAL_USERS_LIST = []

#-----ทำไว้เรียกใช้ข้อมูลใน List-----
def load_users():
    global GLOBAL_USERS_LIST
    return GLOBAL_USERS_LIST

#-----ทำไว้บันทึกข้อมูล-----
def save_users(users_list):
    global GLOBAL_USERS_LIST
    GLOBAL_USERS_LIST = users_list

def open_main_app_window(name):
    all_users = load_users()
    current_user = None
    for user in all_users:
        if user["name"] == name:
            current_user = user
            break

    if current_user is None:
        messagebox.showerror("Error", "ไม่พบข้อมูลผู้ใช้")
        return
#-----Update ผู้ใช้ Realtime-----
    def save_current_user_changes():
        all_users_list = load_users()
        for i, u in enumerate(all_users_list):
            if u["name"] == current_user["name"]:
                all_users_list[i] = current_user 
                break
        else:
            all_users_list.append(current_user)
        
        save_users(all_users_list) 

#-----Tkinter Window-----
    window = tk.Tk()
    window.title("KU+")
    window.geometry("360x660")
    window.resizable(False, False)
    window.configure(bg="#F5F6F7")

#-----ตั้งค่าการตกแต่ง------
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

#-----photo-----
    try:
        ku_img_open = Image.open("Logo_KUplus.png") 
        ku_img_open = ku_img_open.resize((70, 70))
        ku_img = ImageTk.PhotoImage(ku_img_open)
        img_label = ttk.Label(header_frame, image=ku_img, background=bg_main)
        img_label.image = ku_img
        img_label.grid(row=0, column=0, rowspan=2, padx=(0, 15))
    except Exception:
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
        deposit_window.transient(window) 
        deposit_window.grab_set() 

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
                amount_str = amount_var.get().strip()
                if not amount_str: 
                    messagebox.showwarning("Invalid", "Enter a valid amount!", parent=deposit_window)
                    return

                amount = float(amount_str)
                if amount <= 0:
                    messagebox.showwarning("Invalid", "Enter a valid amount!", parent=deposit_window)
                    return
                
                current_user['balance'] += amount
                update_balance_label()
                current_user['transaction'].append(f"Deposited ฿ {amount:,.2f}")
                save_current_user_changes() 
                messagebox.showinfo("Success", f"Successfully deposited ฿ {amount:,.2f}", parent=deposit_window)
                deposit_window.destroy()
            except ValueError:
                messagebox.showwarning("Invalid", "Enter a valid number!", parent=deposit_window)

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
        withdraw_window.transient(window)
        withdraw_window.grab_set()

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
                amount_str = amount_var.get().strip()
                if not amount_str:
                    messagebox.showwarning("Invalid", "Enter a valid amount!", parent=withdraw_window)
                    return

                amount = float(amount_str)
                if amount <= 0:
                    messagebox.showwarning("Invalid", "Enter a valid amount!", parent=withdraw_window)
                    return
                if amount > current_user['balance']:
                    messagebox.showerror("Error", "Insufficient balance", parent=withdraw_window)
                    return
                
                current_user['balance'] -= amount
                update_balance_label()
                current_user['transaction'].append(f"Withdrew ฿ {amount:,.2f}")
                save_current_user_changes() 
                messagebox.showinfo("Success", f"Successfully withdrew ฿ {amount:,.2f}", parent=withdraw_window)
                withdraw_window.destroy()
            except ValueError:
                messagebox.showwarning("Invalid", "Enter a valid number!", parent=withdraw_window)

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

    def show_history():
        history_window = tk.Toplevel(window)
        history_window.title("Transaction History")
        history_window.geometry("360x400")
        history_window.configure(bg="#F5F6F7")
        history_window.attributes("-topmost", 1)
        history_window.resizable(False, False)

        tk.Label(history_window, text="Transaction History", font=("Segoe UI Semibold", 18), fg=k_green, bg="#F5F6F7").pack(pady=(20,10))

        card = tk.Frame(history_window, bg="white", bd=1, relief="ridge")
        card.pack(padx=20, pady=10, fill="both", expand=True)

        transactions = current_user.get('transaction', [])
        if transactions:
            text_frame = tk.Frame(card, bg="white")
            scrollbar = tk.Scrollbar(text_frame, orient="vertical")
            listbox = tk.Listbox(text_frame, yscrollcommand=scrollbar.set, font=("Segoe UI", 12), fg=dark_text, bg="white", activestyle="none", highlightthickness=0, borderwidth=0)
            scrollbar.config(command=listbox.yview)
            
            scrollbar.pack(side="right", fill="y")
            listbox.pack(side="left", fill="both", expand=True, padx=15, pady=10)

            for t in reversed(transactions):
                listbox.insert("end", t)
            
            text_frame.pack(fill="both", expand=True)
        else:
            tk.Label(card, text="No transactions yet.", font=("Segoe UI", 12), fg=dark_text, bg="white").pack(pady=15)

        history_window.transient(window)
        history_window.grab_set()
        window.wait_window(history_window)


    button_frame = ttk.Frame(window, style="App.TFrame", padding=(30, 20))
    button_frame.pack(fill="both", expand=True)

    personal_btn = ttk.Button(button_frame, text="Personal Details", style="App.TButton", command=show_personal_details)
    personal_btn.pack(fill="x", pady=10)

    deposit_btn = ttk.Button(button_frame, text="Deposit", style="App.TButton", command=deposit)
    deposit_btn.pack(fill="x", pady=10)

    withdraw_btn = ttk.Button(button_frame, text="Withdraw", style="App.TButton", command=withdraw)
    withdraw_btn.pack(fill="x", pady=10)

    history_btn = ttk.Button(button_frame, text="History", style="App.TButton", command=show_history)
    history_btn.pack(fill="x", pady=10)

    footer_label = ttk.Label(window, text="KUBank", background=bg_main, foreground="#777777", font=("Segoe UI", 9))
    footer_label.pack(side="bottom", pady=10)

    window.mainloop()

def open_register_window():
#-----ส่วนตั้งค่าการตกแต่ง-----
    k_green = "#00A950"
    light_text = "#FFFFFF"
    dark_text = "#333333"
    bg_white = "#FFFFFF"
    error_text = "yellow"

    def submit():
        
        users = load_users() 
        
        name = name_var.get().strip()
        age = age_var.get().strip()
        gender = gender_var.get().strip()
        password = password_var.get().strip() 

        if name == "" or age == "" or gender == "" or password == "":
            result_label.config(text="All fields are required *", fg=error_text)
            return

        # **ตรวจสอบ Age ต้องเป็นตัวเลข**
        if not age.isdigit():
            result_label.config(text="Age must be a valid number.", fg=error_text)
            return
        
        # เพิ่มการตรวจสอบอายุต้องมากกว่า 0 ด้วย
        if int(age) <= 0:
            result_label.config(text="Age must be greater than 0.", fg=error_text)
            return

        # **ตรวจสอบ Gender ต้องไม่มีตัวเลข**
        if any(char.isdigit() for char in gender):
            result_label.config(text="Gender cannot contain numbers.", fg=error_text)
            return
        
        for user in users:
            if user["name"] == name:
                result_label.config(text="This name is already taken", fg=error_text)
                return

        users_data = {
            "name" : name ,
            "age" : age,
            "gender" : gender,
            "password" : password,
            "balance" : 0.0,
            "transaction" : []
        }

        users.append(users_data)
        save_users(users)
        result_label.config(text="Account has been created", fg=light_text)

        name_var.set("")
        age_var.set("")
        gender_var.set("")
        password_var.set("")

        def close_and_open_launcher():
            window.destroy()
            open_launcher_window()

        window.after(2000, close_and_open_launcher)

#-----หน้าต่างของ register-----
    window = tk.Tk()
    window.title("Register Page")
    window.geometry("360x640")
    window.resizable(False, False)
    window.attributes("-topmost", 1) 
    window.configure(bg=k_green)

    name_var = tk.StringVar(master=window)
    age_var = tk.StringVar(master=window)
    gender_var = tk.StringVar(master=window)
    password_var = tk.StringVar(master=window)

    main_frame = tk.Frame(window, bg=k_green, padx=30, pady=30)
    main_frame.pack(fill="both", expand=True)

#----–หัวเรื่อง-----
    title_label = tk.Label(main_frame, text="Create your account", 
                            font=("Helvetica", 18, "bold"), bg=k_green, fg=light_text)
    title_label.pack(anchor="w", pady=(10, 30))

#-----ช่องใส่ชื่อ-----
    name_label = tk.Label(main_frame, text="Name", 
                            font=("Helvetica", 11), bg=k_green, fg=light_text)
    name_label.pack(anchor="w")
    name_entry = tk.Entry(main_frame, textvariable=name_var, 
                            font=("Helvetica", 12), bg=bg_white, fg=dark_text, 
                            bd=0, relief="flat")
    name_entry.pack(fill="x", pady=(5, 15), ipady=10) 

#-----ช่องใส่อายุ-----
    age_label = tk.Label(main_frame, text="Age", 
                            font=("Helvetica", 11), bg=k_green, fg=light_text)
    age_label.pack(anchor="w")
    age_entry = tk.Entry(main_frame, textvariable=age_var, 
                            font=("Helvetica", 12), bg=bg_white, fg=dark_text, 
                            bd=0, relief="flat")
    age_entry.pack(fill="x", pady=(5, 15), ipady=10)
#-----ช่องใส่เพศ-----
    gender_label = tk.Label(main_frame, text="Gender", 
                                font=("Helvetica", 11), bg=k_green, fg=light_text)
    gender_label.pack(anchor="w")
    gender_entry = tk.Entry(main_frame, textvariable=gender_var, 
                                font=("Helvetica", 12), bg=bg_white, fg=dark_text, 
                                bd=0, relief="flat")
    gender_entry.pack(fill="x", pady=(5, 15), ipady=10)

#-----ช่องใส่ password-----
    password_label = tk.Label(main_frame, text="Password", 
                                    font=("Helvetica", 11), bg=k_green, fg=light_text)
    password_label.pack(anchor="w")
    password_entry = tk.Entry(main_frame, textvariable=password_var, show="*", 
                                    font=("Helvetica", 12), bg=bg_white, fg=dark_text, 
                                    bd=0, relief="flat")
    password_entry.pack(fill="x", pady=(5, 15), ipady=10)

#-----จุดไว้บอกสถานะการ register-----
    result_label = tk.Label(main_frame, text="", 
                                    font=("Helvetica", 12, "bold"), bg=k_green, fg=light_text)
    result_label.pack(pady=(10, 10))

#-----ปุ่มยืนยันการสมัคร-----
    submit_button = tk.Button(main_frame, text="Submit", command=submit, 
                                    font=("Helvetica", 14, "bold"), 
                                    bg=bg_white, fg=k_green,
                                    bd=0, relief="flat", 
                                    activebackground="#E0E0E0",
                                    activeforeground=k_green)
    submit_button.pack(fill="x", pady=20, ipady=10) 

    name_entry.focus()
    window.mainloop()

def open_login_window():
#-----ส่วนตั้งค่าการตกแต่ง-----
    k_green = "#00A950"
    light_text = "#FFFFFF"
    dark_text = "#333333"
    bg_white = "#FFFFFF"
    error_text = "yellow"

    def login():
        login_name = username_var.get().strip()
        login_password = password_var.get().strip()

        users = load_users() 

        for user in users:
            if user["name"] == login_name and user["password"] == login_password:
                result_label.config(text="Login Successful", fg=light_text) 
                
                window.after(1000, lambda: (
                    window.destroy(), 
                    open_main_app_window(user["name"])
                ))
                return
                
        result_label.config(text="Invalid username or password", fg=error_text) 
        username_var.set("")
        password_var.set("")
#-----หน้า Window-----
    window = tk.Tk()
    window.title("KU+ Login Page")
    window.geometry("360x640")
    window.resizable(False, False)
    window.configure(bg=k_green)

    username_var = tk.StringVar(master=window)
    password_var = tk.StringVar(master=window)

    main_frame = tk.Frame(window, bg=k_green, padx=30, pady=30)
    main_frame.pack(fill="both", expand=True)

#-----photo-----
    try:   
        ku_img_open = Image.open("Logo_KUplus.png") 
        ku_img_open = ku_img_open.resize((80, 80))
        ku_img = ImageTk.PhotoImage(ku_img_open)
        img_label = tk.Label(main_frame, image=ku_img, bg=k_green)
        img_label.image = ku_img
        img_label.pack(pady=(20, 10))
    except Exception:
        pass
#-----text-----
    title_label = tk.Label(main_frame, text="Login to your account", 
                            font=("Helvetica", 18, "bold"), bg=k_green, fg=light_text)
    title_label.pack(pady=(10, 30))

    username_label = tk.Label(main_frame, text="Username", 
                                    font=("Helvetica", 11), bg=k_green, fg=light_text)
    username_label.pack(anchor="w")
    username_entry = tk.Entry(main_frame, textvariable=username_var,
                                    font=("Helvetica", 12), bg=bg_white, fg=dark_text, 
                                    bd=0, relief="flat")
    username_entry.pack(fill="x", pady=(5, 15), ipady=10)

    password_label = tk.Label(main_frame, text="Password", 
                                    font=("Helvetica", 11), bg=k_green, fg=light_text)
    password_label.pack(anchor="w")
    password_entry = tk.Entry(main_frame, textvariable=password_var, show="*",
                                    font=("Helvetica", 12), bg=bg_white, fg=dark_text, 
                                    bd=0, relief="flat")
    password_entry.pack(fill="x", pady=(5, 15), ipady=10)

    result_label = tk.Label(main_frame, text="", 
                                    font=("Helvetica", 12, "bold"), bg=k_green, fg=light_text)
    result_label.pack(pady=(10, 10))

#-----button-----
    login_button = tk.Button(main_frame, text="Login", command=login,
                                    font=("Helvetica", 14, "bold"), 
                                    bg=bg_white, fg=k_green,
                                    bd=0, relief="flat",
                                    activebackground="#E0E0E0",
                                    activeforeground=k_green)
    login_button.pack(fill="x", pady=20, ipady=10)

    username_entry.focus()
    window.mainloop()

def open_launcher_window():
    def login():
        window.destroy()
        open_login_window()

    def register():
        window.destroy()
        open_register_window()

    window = tk.Tk()
    window.title("KU PLUS Bank Application")
    window.geometry("340x460")
    window.resizable(False, False)
    window.configure(bg="#006A4E")

    try:
        logo_img_open = Image.open("Logo_KUplus.png")
        logo_img_open = logo_img_open.resize((120, 120))
        logo_img = ImageTk.PhotoImage(logo_img_open)
    except Exception:
        # ใช้เฟรมเปล่าแทนถ้าหาไฟล์รูปไม่เจอ
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
        img_label.image = logo_img 
        img_label.pack(pady=(40, 10))
    else:
        # Placeholder ถ้าไม่มีรูป
        tk.Label(window, text="[KU PLUS LOGO]", font=("Segoe UI", 16), bg="#006A4E", fg="white").pack(pady=(40, 10))

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

if __name__ == "__main__":
    open_launcher_window()