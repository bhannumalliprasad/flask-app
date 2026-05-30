from flask import Blueprint
from controllers.authController import register, login, profile
from middlewares.authMiddleware import token_required

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/register', methods=['POST'])(register)
auth_bp.route('/login', methods=['POST'])(login)
auth_bp.route('/profile', methods=['GET'])(token_required(profile))