from fastapi import FastAPI
from api.cart import cart_router  # Add the extra '.'
from api.checkout import checkout_router
from api.admin import admin_router

app = FastAPI()

app.include_router(cart_router, prefix="/cart")
app.include_router(checkout_router, prefix="/checkout")
app.include_router(admin_router, prefix="/admin")
