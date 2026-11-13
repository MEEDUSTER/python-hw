from product import Product


class ProductModel:
    def __init__(self):
        self.products = []
        self.create_product(Product(
            1,
            "Ноутбук",
            "https://picsum.photos/id/0/400/300",
            25000,
            4.5,
        ))
        self.create_product(Product(
            2,
            "Смартфон",
            "https://picsum.photos/id/1/400/300",
            15000,
            4.8,
        ))
        self.create_product(Product(
            3,
            "Навушники",
            "https://picsum.photos/id/3/400/300",
            3000,
            4.2,
        ))

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def create_product(self, product):
        self.products.append(product)
        return product
