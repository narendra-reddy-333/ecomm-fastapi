from fastapi import APIRouter, HTTPException

from api.models import CartItem

cart = []  # In-memory cart storage

cart_router = APIRouter()


@cart_router.post("/add-item")
def add_to_cart(item: CartItem):
    cart.append(item)
    return {"message": "Item added to cart"}
