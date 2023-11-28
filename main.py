from tkinter import Tk
from services.auth_service import AuthService
from views.login_view import LoginView
from views.product_list_view import ProductListView

class MainApp:
    def __init__(self):
        #窗口不应该由入口文件维护，由页面组件自己维护，会设计到不同页面组件的销毁和新建
        self.root = Tk()
        self.root.title("TKinter App")

        self.auth_service = AuthService()

        if self.auth_service.is_user_logged_in():
            self.show_product_list()
        else:
            self.show_login()

    def show_login(self):
        login_view = LoginView(self.root, self.auth_service)
        login_view.show()

    def show_product_list(self):
        product_list_view = ProductListView()
        product_list_view.show()

    def run(self):
        self.root.mainloop()

app = MainApp()
app.run()
