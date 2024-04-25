import uuid  # For code generation

from fastapi import APIRouter, HTTPException

from .models import Order, DiscountCode

admin_router = APIRouter()

orders = []  # In-memory order history


@admin_router.get("/stats")
def get_stats():
    def calculate_order_amount(order: Order) -> float:
        """Calculates the total amount of an order, applying any discount.

        Assumptions:
        * Product prices are not stored separately; you'll need a way to retrieve them.
        """

        total_amount = sum(item.product_id * item.quantity for item in
                           order.cart_items)  # Replace product_id with how you retrieve the price

        if order.discount_code:
            discount = 0.1 * total_amount
            total_amount -= discount

        return total_amount

    total_items = sum(sum(order.cart_items, []).quantity for order in orders)
    total_amount = sum(calculate_order_amount(order) for order in orders)  # Implement calculate_order_amount as needed
    discounts = [code for code in orders if code.discount_code]
    total_discount = sum(0.1 * calculate_order_amount(order) for order in discounts)

    return {
        "total_items_purchased": total_items,
        "total_purchase_amount": total_amount,
        "discount_codes": [code.code for code in discounts],
        "total_discount_amount": total_discount
    }


@admin_router.post("/generate-discount")  # New endpoint
def generate_discount():
    global available_discount

    if available_discount:
        raise HTTPException(status_code=400, detail="Discount code already exists")

    available_discount = DiscountCode(code=str(uuid.uuid4())[:8])
    return {"message": "Discount code generated", "code": available_discount.code}
