import tkinter
import re

from tkinter import messagebox


class Menu(object):

    def __init__(self):
        self.is_end = False
        self.is_execute = False
        self.main_win = tkinter.Tk()
        self.main_win.title("Roullet Player 起動画面")
        self.main_win.geometry('500x200')

        label_for_mail = tkinter.Label(text='メールアドレス')
        label_for_mail.place(x=10, y=30)
        self.input_mail = tkinter.Entry(width=50)
        self.input_mail.place(x=100, y=30)

        label_for_pass = tkinter.Label(text='パスワード')
        label_for_pass.place(x=10, y=80)
        self.input_password = tkinter.Entry(show='*', width=50)
        self.input_password.place(x=100, y=80)

        """label_for_base_amount = tkinter.Label(text='ベット単位')
        label_for_base_amount.place(x=10, y=130)
        self.input_base_amount = tkinter.Entry(width=50)
        self.input_base_amount.place(x=100, y=130)"""

        """label_for_roop_num = tkinter.Label(text='セット数')
        label_for_roop_num.place(x=10, y=180)
        self.input_roop_num = tkinter.Entry(width=50)
        self.input_roop_num.place(x=100, y=180)"""

        btn = tkinter.Button(self.main_win, text='実行', command=self.execute)
        btn.place(x=250, y=130)

        """btn = tkinter.Button(self.main_win, text='終了', command=self.end)"""
        """btn.place(x=300, y=130)"""

        self.main_win.mainloop()

    def execute(self):
        if not self.input_mail.get():
            self.show_error_message_blank_mailaddress()
            return None
        if self.is_mailaddress_ok(self.input_mail.get()) is not True:
            self.show_error_message_invalid_mailaddress()
            return None
        self.mail = self.input_mail.get()

        if not self.input_password.get():
            self.show_error_message_blank_password()
            return None
        self.password = self.input_password.get()
        self.is_execute = True
        self.main_win.destroy()
        """self.base_amount = self.input_base_amount.get()"""
        """self.roop_num = self.input_roop_num.get()"""

    def end(self):
        if not self.execute:
            messagebox.showerror('エラー', '実行前に終了することはできません。')
        self.is_end = True
        self.main_win.destroy()

    def get_user_info(self):
        """return {"mail":self.mail, "password": self.password, "base_amount":self.base_amount, "roop_num":self.roop_num}"""
        return {"mail": self.mail, "password": self.password}
    
    def get_is_end(self):
        return self.is_end
    
    def get_is_execute(self):
        return self.is_execute

    def is_mailaddress_ok(self, mailaddress):
        pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, mailaddress):
            return False
        return True

    def is_password_ok(password):
        if password is None:
            return False
        return True

    def show_error_message_blank_mailaddress(self):
        messagebox.showerror('エラー', 'メールアドレスを入力してください。')

    def show_error_message_blank_password(self):
        messagebox.showerror('エラー', 'パスワードを入力してください。')

    def show_error_message_invalid_mailaddress(self):
        messagebox.showerror('エラー', 'メールアドレスが正しくありません。')

    def show_error_message_cannot_login(self):
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showerror('エラー', 'ログインできませんでした。')
