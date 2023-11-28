from models import User
import json
import os

# 定义文件路径常量
LOGIN_INFO_PATH = os.path.join("data", "login_info.json")

class AuthService:
    def __init__(self):
        self.logged_in_user = None

    def is_user_logged_in(self):
        username=self.load_login_info()
        return self.logged_in_user is not None or  username is not None

    def login(self, username, password):
        # 调用其他模块的函数来验证用户名和密码
        user = User(username, password)
        if self.authenticate(user):
            self.logged_in_user =user
            self.save_login_info(username)
            return True
        else:
            return False
    # 保存登录信息到文件
    def save_login_info(self,username):
        data = {"username": username}
        try:
            with open(LOGIN_INFO_PATH, "w") as file:
                json.dump(data, file)
        except FileNotFoundError:
                    return None
    # 从文件加载登录信息
    def load_login_info(self):
        try:
            with open(LOGIN_INFO_PATH, "r") as file:
                data = json.load(file)
                return data["username"]
        except FileNotFoundError:
            return None
    def authenticate(self, user):
        return True
        # 调用其他模块的函数来验证用户名和密码的正确性
        pass
