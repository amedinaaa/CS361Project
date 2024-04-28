from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cart/")
def cart():
    return render_template("cart.html")



@app.route("/product/")

@app.route("/product/<name>")
def product(name = None):
    return render_template(
        "product.html",
        name=name,
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")