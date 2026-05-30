from flask import request, jsonify
from config import db
from bson import ObjectId

products = db["products"]


def add_product():
    data = request.json

    product = {
        "title": data.get("title"),
        "description": data.get("description"),
        "price": data.get("price")
    }

    result = products.insert_one(product)

    return jsonify({
        "message": "Product added successfully",
        "product_id": str(result.inserted_id)
    })


def get_products():
    all_products = []

    for product in products.find():
        all_products.append({
            "id": str(product["_id"]),
            "title": product["title"],
            "description": product["description"],
            "price": product["price"]
        })

    return jsonify(all_products)


def get_single_product(id):
    product = products.find_one({
        "_id": ObjectId(id)
    })

    if not product:
        return jsonify({
            "message": "Product not found"
        }), 404

    return jsonify({
        "id": str(product["_id"]),
        "title": product["title"],
        "description": product["description"],
        "price": product["price"]
    })


def update_product(id):
    data = request.json

    products.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "title": data.get("title"),
                "description": data.get("description"),
                "price": data.get("price")
            }
        }
    )

    return jsonify({
        "message": "Product updated successfully"
    })

def delete_product(id):
    products.delete_one({
        "_id": ObjectId(id)
    })

    return jsonify({
        "message": "Product deleted successfully"
    })