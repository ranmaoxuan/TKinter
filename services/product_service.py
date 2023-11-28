from models import Product

class ProductService:
    def __init__(self):
        self.products = [
            Product("Product 1", 10),
            Product("Product 2", 20),
            Product("Product 3", 30)
        ]

    def get_product_list(self):
        return self.products

    def get_product_details(self, product_id):
        # 根据商品ID获取商品详情的代码省略
        pass
