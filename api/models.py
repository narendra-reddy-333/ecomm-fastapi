from pydantic import BaseModel
import uuid

from api.constants import DISCOUNT_PERCENTAGE


class CartItem(BaseModel):
    product_id: int
    quantity: int
    price: float


class Order(BaseModel):
    items: list[CartItem]
    discount_code: str | None = None
    total_price: float = 0


class DiscountCode(BaseModel):
    code: str
    discount_percentage: float = DISCOUNT_PERCENTAGE

