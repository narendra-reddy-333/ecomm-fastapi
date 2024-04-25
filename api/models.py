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


class AddToCartResponse(BaseModel):
    message: str


class CheckoutResponse(BaseModel):
    message: str
    order: Order
    discount: float


class AdminStatsResponse(BaseModel):
    total_items_purchased: int
    total_purchase_amount: float
    discount_codes: list[str]
    total_discount_amount: float


class GenerateDiscountResponse(BaseModel):
    message: str
    code: str  # Or you could return the entire DiscountCode model
