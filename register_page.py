import tkinter as tk
from tkinter import messagebox
import psycopg2
import hashlib


class RegisterPage:
    def __init__(self, root, db):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.db = db

        self.create_username_label = tk.Label(self.frame, text="Create Username")
        self.create_username_label.pack()
        self.create_username_input = tk.Entry(self.frame)
        self.create_username_input.pack()

        self.create_password_label = tk.Label(self.frame, text="Create Password")
        self.create_password_label.pack()
        self.create_password_input = tk.Entry(self.frame, show="*")
        self.create_password_input.pack()

        self.register_button = tk.Button(self.frame, text="Register", command=self.create_account)
        self.register_button.pack()

    def execute_sql(self, sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def create_account(self):
        create_username = self.create_username_input.get()
        create_password = self.create_password_input.get()
        if create_username and create_password:
            create_password_hash = hashlib.sha256(create_password.encode()).hexdigest()
            try:
                sql = f'''
                    INSERT INTO users (id, username, password)
                    VALUES ((select count(*)+1 from users), '{create_username}', '{create_password_hash}')
                '''
                self.execute_sql(sql)
                self.db.commit()
                self.create_username_input.delete(0, tk.END)
                self.create_password_input.delete(0, tk.END)
                messagebox.showinfo("Account created", "Account created successfully.")
            except psycopg2.IntegrityError:
                messagebox.showerror("Username already in use.", "Username already in use.")
