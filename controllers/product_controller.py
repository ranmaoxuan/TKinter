from services.product_service import ProductService

class ProductController:
    def __init__(self):
        self.product_service = ProductService()

    def get_product_list(self):
        return self.product_service.get_product_list()

    def get_product_details(self, product_id):
        return self.product_service.get_product_details(product_id)
