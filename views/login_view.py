from tkinter import Tk, ttk, StringVar, messagebox
from controllers.login_controller import LoginController
from views.product_list_view import ProductListView

class LoginView:
    def __init__(self, root, auth_service):
        self.root = root
        self.auth_service = auth_service

        self.controller = LoginController(auth_service)
        self.create_login_page()

    def create_login_page(self):
        self.frm = ttk.Frame(self.root, padding=20)
        self.frm.grid()

        # 界面元素的创建代码省略
        frm = ttk.Frame(self.root, padding=20)
        frm.grid()

        account_frm = ttk.Frame(frm, padding=10)
        account_frm.grid()

        ttk.Label(account_frm, text="User Name:").grid(column=0, row=0, sticky='w')

        self.username = StringVar()
        username_entry = ttk.Entry(account_frm, width=20, textvariable=self.username)
        username_entry.grid(column=1, row=0)


        pass_frm = ttk.Frame(frm, padding=10)
        pass_frm.grid()
        ttk.Label(pass_frm, text="Password:").grid(column=0, row=0, sticky='w')
        self.password = StringVar()
        password_entry = ttk.Entry(pass_frm, width=20, textvariable=self.password, show="*")
        password_entry.grid(column=1, row=0)


        button_frm = ttk.Frame(frm, padding=0)
        button_frm.grid()
        ttk.Button(button_frm, text="Login", command=self.login).grid(column=0, row=0, pady=30)


        # ttk.Button(self.frm, text="Login", command=self.login).grid(column=0, row=0, pady=30)

    def login(self):
        print(self)
        username = self.username.get()
        password = self.password.get()

        if self.controller.login(username, password):
            messagebox.showinfo("登录成功", "登录成功！")
            self.destroy()
            # self.controller.show_product_list()
            # ProductListView.show();
            product_list_view = ProductListView()
            product_list_view.show()

            # self.product_list_view.show()
        else:
            messagebox.showerror("登录失败", "用户名或密码错误！")

    def show(self):
        self.root.mainloop()

    def destroy(self):
        self.root.destroy()
