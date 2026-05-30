from flask import request, jsonify
from config import db

orders = db["orders"]


def my_orders():
    user_id = request.user["user_id"]

    user_orders = []

    for order in orders.find({
        "user_id": user_id
    }):
        user_orders.append({
            "id": str(order["_id"]),
            "product_id": order["product_id"],
            "payment_id": order["payment_id"],
            "status": order["status"]
        })

    return jsonify(user_orders)