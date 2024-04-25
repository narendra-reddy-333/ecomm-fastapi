from datetime import datetime


class CartItem:
    def __init__(self, product_id: int, quantity: int):
        self.product_id = product_id
        self.quantity = quantity


class Order:
    def __init__(self, cart_items: list[CartItem], discount_code: str = None):
        self.cart_items = cart_items
        self.discount_code = discount_code
        self.order_time = datetime.now()


class DiscountCode:
    def __init__(self, code: str, is_used: bool = False):
        self.code = code
        self.is_used = is_used
