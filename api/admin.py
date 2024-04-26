import uuid

from fastapi import APIRouter

from .cart import order_history
from .constants import DISCOUNT_PERCENTAGE

admin_router = APIRouter()


@admin_router.post("/discount")
async def generate_discount():
    global current_discount_code
    current_discount_code = str(uuid.uuid4())[:8].upper()
    return {"code": current_discount_code}


@admin_router.get("/stats")
async def get_stats():
    total_items = sum(item.quantity for order in order_history for item in order.items)
    total_purchase_amount = sum(order.total_price for order in order_history)
    discount_codes = [order.discount_code for order in order_history if order.discount_code]
    total_discount_amount = sum(DISCOUNT_PERCENTAGE * order.total_price for order in order_history if order.discount_code)
    return {
        "total_items": total_items,
        "total_purchase_amount": total_purchase_amount,
        "discount_codes": discount_codes,
        "total_discount_amount": total_discount_amount
    }
