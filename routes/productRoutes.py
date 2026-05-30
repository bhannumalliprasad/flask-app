from flask import Blueprint
from controllers.productController import (
    add_product,
    get_products,
    get_single_product,
    update_product,
    delete_product
)
from middlewares.authMiddleware import token_required

product_bp = Blueprint('products', __name__)

product_bp.route('/products', methods=['POST'])(token_required(add_product))
product_bp.route('/products', methods=['GET'])(get_products)
product_bp.route('/products/<id>', methods=['GET'])(get_single_product)
product_bp.route('/products/<id>', methods=['PUT'])(token_required(update_product))
product_bp.route('/products/<id>', methods=['DELETE'])(token_required(delete_product))