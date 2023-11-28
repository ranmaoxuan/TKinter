
from views.product_list_view import ProductListView


class LoginController:
    def __init__(self, auth_service):
        self.auth_service = auth_service


    def login(self, username, password):
        return self.auth_service.login(username, password)

    def show_product_list(self):
        # 调用其他模块的函数来显示商品列表
        # product_list_view = ProductListView(MainApp.root)
        # product_list_view.show()
        pass
