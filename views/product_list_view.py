from controllers.product_controller import ProductController
from tkinter import Tk, StringVar, ttk, messagebox

class ProductListView:
    def __init__(self):
        self.root = Tk()
        self.root.title("My App")
        self.controller = ProductController()

    def show(self):
        print(123)
        self.frm = ttk.Frame(self.root, padding=20)
        self.frm.grid()

        # 界面元素的创建代码省略
        # 创建商品列表
        product_list = ttk.Treeview(self.frm, columns=("name", "price"), show="headings")
        product_list.heading("name", text="商品名称")
        product_list.heading("price", text="价格")
        product_list.grid()

        # 添加示例商品数据
        product_list.insert("", "end", values=("商品1", "$10"))
        product_list.insert("", "end", values=("商品2", "$20"))
        product_list.insert("", "end", values=("商品3", "$30"))

        # 绑定单击事件，查看商品详情
        product_list.bind("<Double-1>", self.show_product_details)
        self.load_product_list()
        self.root.mainloop()
    def load_product_list(self):
        product_list = self.controller.get_product_list()

        # 将商品列表显示在界面上的代码省略
    def show_product_details(self,event):
        selection = event.widget.selection()
        if selection:
            item = event.widget.item(selection)
            product_name = item["values"][0]
            messagebox.showinfo("商品详情", f"商品名称：{product_name}\n商品详细信息：这是{product_name}的详细信息。")
