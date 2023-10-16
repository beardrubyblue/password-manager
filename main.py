import tkinter as tk
import psycopg2
import hashlib


class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        root.title("Password Manager")

        self.current_user_id = None

        self.login_frame = tk.Frame(root)
        self.login_frame.pack()

        self.username_label = tk.Label(self.login_frame, text="Username")
        self.username_label.pack()
        self.username_input = tk.Entry(self.login_frame)
        self.username_input.pack()

        self.password_label = tk.Label(self.login_frame, text="Password")
        self.password_label.pack()
        self.password_input = tk.Entry(self.login_frame, show="*")
        self.password_input.pack()

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.pack()

        self.main_frame = tk.Frame(root)

        self.password_label = tk.Label(self.main_frame, text="Enter Password")
        self.password_label.pack()
        self.password_input_view = tk.Entry(self.main_frame, show="*")
        self.password_input_view.pack()

        self.add_password_button = tk.Button(self.main_frame, text="Add Password", command=self.add_password)
        self.add_password_button.pack()

        self.delete_password_button = tk.Button(self.main_frame, text="Delete Password", command=self.delete_password)
        self.delete_password_button.pack()

        self.conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="152733",
            host="localhost",
            port="5432"
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT, email TEXT)''')
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS passwords (id SERIAL PRIMARY KEY, user_id INTEGER, service_name TEXT, password TEXT)''')
        self.conn.commit()

        self.login_frame.tkraise()

    def login(self):
        username = self.username_input.get()
        password = self.password_input.get()
        if username and password:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            self.cursor.execute("SELECT id FROM users WHERE username = %s AND password_hash = %s",
                                (username, password_hash))
            user_id = self.cursor.fetchone()
            if user_id:
                self.current_user_id = user_id[0]
                self.username_input.delete(0, tk.END)
                self.password_input.delete(0, tk.END)
                self.login_frame.pack_forget()
                self.main_frame.pack()
                self.refresh_password_list()
                print("Logged in successfully.")
            else:
                print("Invalid credentials.")

    def add_password(self):
        service_name = self.password_input_view.get()
        password = self.password_input.get()
        if service_name and password and self.current_user_id:
            self.cursor.execute("INSERT INTO passwords (user_id, service_name, password) VALUES (%s, %s, %s)",
                                (self.current_user_id, service_name, password))
            self.conn.commit()
            self.password_input_view.delete(0, tk.END)
            self.refresh_password_list()
            print("Password added successfully.")

    def delete_password(self):
        selected_item = self.password_listbox.curselection()
        if selected_item and self.current_user_id:
            password_id = selected_item[0]
            self.cursor.execute("DELETE FROM passwords WHERE id = %s AND user_id = %s",
                                (password_id, self.current_user_id))
            self.conn.commit()
            self.refresh_password_list()
            print("Password deleted.")

    def refresh_password_list(self):
        self.password_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT id, service_name FROM passwords WHERE user_id = %s", (self.current_user_id,))
        password_list = self.cursor.fetchall()
        for item in password_list:
            self.password_listbox.insert(tk.END, item[1])


if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()