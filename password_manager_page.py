import tkinter as tk


class PasswordManagerPage:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)

        self.title_label = tk.Label(self.frame, text="Password Manager")
        self.title_label.pack()

        self.password_label = tk.Label(self.frame, text="Password:")
        self.password_label.pack()
        self.password_input = tk.Entry(self.frame, show="*")
        self.password_input.pack()

        self.add_password_button = tk.Button(self.frame, text="Add Password", command=self.add_password)
        self.add_password_button.pack()

    def add_password(self):
        # Здесь вы можете добавить функциональность для добавления пароля в менеджер
        # Например, сохранить пароль в базе данных и отобразить список сохраненных паролей

        # Пример сохранения пароля в базе данных:
        new_password = self.password_input.get()
        # Здесь вы можете выполнить SQL-запрос для сохранения пароля в базе данных

if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordManagerPage(root)
    root.mainloop()
