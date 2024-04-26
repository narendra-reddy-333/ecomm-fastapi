import uuid

from fastapi import APIRouter, HTTPException

from .constants import DISCOUNT_PERCENTAGE, NTH_ORDER
from .models import CartItem, Order, DiscountCode

cart_router = APIRouter()

cart = []  # In-memory cart
order_history = []
order_count = 0
current_discount_code = None


def calculate_total_price(order: Order):
    """
    Calculate the total price of a given order
    :param order: order to calculate the total price for
    :return: total price
    """
    total = sum(item.price * item.quantity for item in order.items)
    if order.discount_code and order.discount_code == current_discount_code:
        total *= (1 - DiscountCode.discount_percentage)
    return total


@cart_router.post("/cart/items")
async def add_item_to_cart(item: CartItem):
    cart.append(item)
    return {"message": "Item added to cart"}


@cart_router.post("/checkout")
async def checkout():
    global order_count, current_discount_code

    if not cart:
        raise HTTPException(status_code=400, detail="Cart is empty")

    order = Order(items=cart)  # Create order from cart items
    order_count += 1

    order.total_price = calculate_total_price(order)

    if order_count % NTH_ORDER == 0:  # if every nth order , we give discount on cart.
        current_discount_code = str(uuid.uuid4())[:8]
        order.discount_code = current_discount_code

    order_history.append(order)
    cart.clear()
    response = {"message": "Order placed successfully", "total_price": order.total_price}
    if order.discount_code:
        discount_amount = order.total_price * DISCOUNT_PERCENTAGE
        response.update({"discount_applied": True, "discount_amount": discount_amount})
    else:
        response.update({"discount_applied": False})
    return response
