from fastapi import APIRouter

from api.models import CartItem, AddToCartResponse

cart = []  # In-memory cart storage

cart_router = APIRouter()


@cart_router.post("/add-item")
def add_to_cart(item: CartItem):
    cart.append(item)
    return AddToCartResponse(message="Item added to cart")  # Return the response model

