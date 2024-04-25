from datetime import datetime
from pydantic import BaseModel, Field


class CartItem(BaseModel):
    product_id: int
    quantity: int
    price: float


class Order(BaseModel):
    cart_items: list[CartItem]
    discount_code: str = None
    order_time: datetime = Field(default_factory=datetime.now)


class DiscountCode(BaseModel):
    code: str
    is_used: bool = False
