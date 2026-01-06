from .money import Money


class OrderLine:
    def __init__(self, product: str, price: Money):
        self.product = product
        self.price = price
