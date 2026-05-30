from flask import Blueprint
from controllers.orderController import my_orders
from middlewares.authMiddleware import token_required

order_bp = Blueprint('orders', __name__)

order_bp.route('/my-orders', methods=['GET'])(token_required(my_orders))