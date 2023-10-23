import tkinter as tk
from tkinter import ttk
import psycopg2
from login_page import LoginPage
from register_page import RegisterPage
from password_manager_page import PasswordManagerPage


class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        root.title("Password Manager")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        db_config = {
            'database': 'postgres',
            'user': 'postgres',
            'password': '152733',
            'host': 'localhost',
            'port': '5432'
        }
        self.db = psycopg2.connect(**db_config)

        login_page = LoginPage(self.notebook, self.db)
        self.notebook.add(login_page.frame, text='Login')

        register_page = RegisterPage(self.notebook, self.db)
        self.notebook.add(register_page.frame, text='Register')

        password_manager_page = PasswordManagerPage(self.notebook)
        self.notebook.add(password_manager_page.frame, text='Password Manager')


if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
