from flask import Flask,render_template
from routes.authRoutes import auth_bp
from routes.productRoutes import product_bp
from routes.paymentRoutes import payment_bp
from routes.orderRoutes import order_bp
from apiflask import APIFlask

app = APIFlask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(order_bp)


@app.route('/')
def home():
    return {
        "message": "SkillKart API Running"
    }


@app.route('/payment-page')
def payment_page():
    return render_template("payment.html")

@app.route('/map')
def map_page():
    return render_template("map.html")


if __name__ == '__main__':
    app.run(debug=True)