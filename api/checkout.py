import uuid

from fastapi import APIRouter, HTTPException
from .models import Order, DiscountCode
from .cart import cart  # Import the in-memory cart

checkout_router = APIRouter()

NTH_ORDER_DISCOUNT = 3  # Trigger discount every 3 orders
current_order_count = 0
available_discount = None


# ... previous code ...

@checkout_router.post("/checkout")
async def checkout(discount_code: str = None):  # Make checkout async-ready
    global current_order_count, available_discount, cart, orders

    current_order_count += 1

    # Generate a new discount code if applicable
    if current_order_count % NTH_ORDER_DISCOUNT == 0:
        available_discount = DiscountCode(code=str(uuid.uuid4())[:8])

        # Validation
    if discount_code and available_discount and not available_discount.is_used:
        if discount_code == available_discount.code:
            discount = 0.1  # Apply 10% discount
        else:
            raise HTTPException(status_code=400, detail="Invalid discount code")
    else:
        discount = 0

    order = Order(cart_items=cart.copy(), discount_code=discount_code)
    orders.append(order)

    # Mark discount as used
    if available_discount and available_discount.code == discount_code:
        available_discount.is_used = True

    cart.clear()  # Clear cart after successful checkout
    return {
        "message": "Order placed",
        "order": order.__dict__,  # Return order details (modify if needed)
        "discount": discount
    }
