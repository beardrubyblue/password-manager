import tkinter as tk
from tkinter import messagebox
import hashlib


class LoginPage:
    def __init__(self, root, db):
        self.logged_in = None
        self.current_user_id = None
        self.root = root
        self.frame = tk.Frame(self.root)
        self.db = db

        self.username_label = tk.Label(self.frame, text="Username")
        self.username_label.pack()
        self.username_input = tk.Entry(self.frame)
        self.username_input.pack()

        self.password_label = tk.Label(self.frame, text="Password")
        self.password_label.pack()
        self.password_input = tk.Entry(self.frame, show="*")
        self.password_input.pack()

        self.login_button = tk.Button(self.frame, text="Login", command=self.login)
        self.login_button.pack()

    def execute_sql(self, sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def login(self):
        username = self.username_input.get()
        password = self.password_input.get()
        if username and password:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            sql = f'''
                SELECT id from users 
                WHERE username = '{username}' AND password = '{password_hash}'
            '''
            user_id = self.execute_sql(sql)
            if user_id:
                self.current_user_id = user_id[0][0]
                self.logged_in = True
                self.username_input.delete(0, tk.END)
                self.password_input.delete(0, tk.END)
                messagebox.showinfo("Login Successful", "Logged in successfully.")
            else:
                messagebox.showerror("Login Failed", "Invalid credentials.")
