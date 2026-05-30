from flask import request, jsonify
from config import db
import bcrypt
from utils.jwtHelper import generate_token
from bson import ObjectId

users = db["users"]


def register():
    data = request.json

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    existing_user = users.find_one({
        "email": email
    })

    if existing_user:
        return jsonify({
            "message": "Email already exists"
        }), 400

    hashed_password = bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    )

    user = {
        "name": name,
        "email": email,
        "password": hashed_password
    }

    result = users.insert_one(user)

    return jsonify({
        "message": "User registered successfully",
        "user_id": str(result.inserted_id)
    })


def login():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    user = users.find_one({
        "email": email
    })

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    password_match = bcrypt.checkpw(
        password.encode('utf-8'),
        user["password"]
    )

    if not password_match:
        return jsonify({
            "message": "Invalid password"
        }), 401

    token = generate_token(user["_id"])

    return jsonify({
        "message": "Login successful",
        "token": token
    })


def profile():
    user_id = request.user["user_id"]

    user = users.find_one({
        "_id": ObjectId(user_id)
    })

    return jsonify({
        "name": user["name"],
        "email": user["email"]
    })