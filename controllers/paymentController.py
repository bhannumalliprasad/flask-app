from flask import request, jsonify
from config import db
from bson import ObjectId
import razorpay
import os

products = db["products"]
orders = db["orders"]

client = razorpay.Client(auth=(
    os.getenv("RAZORPAY_KEY_ID"),
    os.getenv("RAZORPAY_KEY_SECRET")
))


def create_order():
    data = request.json

    product_id = data.get("product_id")

    product = products.find_one({
        "_id": ObjectId(product_id)
    })

    if not product:
        return jsonify({
            "message": "Product not found"
        }), 404

    amount = int(product["price"] * 100)

    razorpay_order = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": 1
    })

    return jsonify({
        "razorpay_order_id": razorpay_order["id"],
        "amount": amount,
        "product_name": product["title"],
        "key": os.getenv("RAZORPAY_KEY_ID")
    })


def verify_payment():
    data = request.json

    user_id = request.user["user_id"]

    order = {
        "user_id": user_id,
        "product_id": data.get("product_id"),
        "payment_id": data.get("razorpay_payment_id"),
        "order_id": data.get("razorpay_order_id"),
        "status": "paid"
    }

    result = orders.insert_one(order)

    return jsonify({
        "message": "Payment Verified Successfully",
        "db_order_id": str(result.inserted_id)
    })