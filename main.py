from fastapi import FastAPI

from api.admin import admin_router
from api.cart import cart_router

app = FastAPI()

app.include_router(cart_router, prefix="/api")
app.include_router(admin_router, prefix="/api/admin")


@app.get("/")
async def root():
    return {"message": "Welcome to the Ecommerce API"}
