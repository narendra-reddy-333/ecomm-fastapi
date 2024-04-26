## Ecommerce API with FastAPI - README

### Project Overview

This project implements a simple e-commerce store backend API using FastAPI. It provides functionalities for managing a shopping cart, processing orders, and generating discount codes. The API includes endpoints for:

*   **Cart Management:**
    *   Adding items to the cart.
    *   Checking out with the current cart contents.
*   **Order Processing:**
    *   Calculating the total order price, including discounts.
    *   Generating and applying discount codes for every nth order.
*   **Admin Functionality:**
    *   Generating new discount codes on demand.
    *   Retrieving store statistics such as total items sold, purchase amount, and discount usage.

### API Endpoints

**Cart Management:**

*   **POST `/api/cart/items`**
    *   Adds an item to the cart.
    *   Request Body:
    ```json
    {
      "product_id": 123,
      "quantity": 2,
      "price": 10.99
    }
    ```
*   **POST `/api/checkout`**
    *   Processes the order with the current cart contents.
    *   Response Body (Example with Discount):
    ```json
    {
      "message": "Order placed successfully",
      "total_price": 80.0,
      "discount_applied": true,
      "discount_amount": 10.0
    }
    ```

**Admin Functionality:**

*   **POST `/api/admin/discount`**
    *   Generates a new random alphanumeric discount code. 
    *   Response Body:
    ```json
    {
      "code": "A7cD3f2b" 
    }
    ```
*   **GET `/api/admin/stats`**
    *   Retrieves store statistics.
    *   Response Body:
    ```json
    {
      "total_items": 120,
      "total_purchase_amount": 1500.0,
      "discount_codes": ["CODE1", "CODE2", "..."],
      "total_discount_amount": 75.0
    }
    ```

### Running the Application

1.  **Clone the repository:** `git clone https://github.com/your-username/ecommerce_api.git`
2.  **Install dependencies:** `pip install fastapi uvicorn`
3.  **Run the application:** `uvicorn main:app --reload`
4.  **Access the API documentation:** `http://localhost:8000/docs` (use this as Postman equivalent)

### Testing

You can use tools like FastAPI docs or Postman or curl to interact with the API endpoints and test the functionality.

### Technology Stack

*   **FastAPI:** Python web framework for building APIs.
*   **Uvicorn:** ASGI server for running FastAPI applications.
*   **Pydantic:** Library for data validation and parsing.