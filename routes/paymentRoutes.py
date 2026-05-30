from flask import Blueprint
from controllers.paymentController import create_order, verify_payment
from middlewares.authMiddleware import token_required

payment_bp = Blueprint('payment', __name__)

payment_bp.route('/create-order', methods=['POST'])(token_required(create_order))
payment_bp.route('/verify-payment', methods=['POST'])(token_required(verify_payment))