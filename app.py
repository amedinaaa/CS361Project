from flask import Flask, request, render_template
import json

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# class products(db.Model):
#     _id = db.Column("id", db.Integer, primary_key=True)
#     name = db.Column(db.string(50))
#     price = db.Column(db.Float(4))
#     image = db.Column(db.string(100))
#     specifications = db.Column(db.string(300))

#     def __init__(self, name, price, image, specifications):
#         self.name = name
#         self.price = price,
#         self.image = image,
#         self.specifications = specifications


if __name__=="__main__":
        app.run(debug=True)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cart/")
def cart():
    return render_template("cart.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/search", methods=["GET"])
def search():
     query = request.args.get("query")
     if not query:
        #   return render_template(
        #        "results.html",
        #        name=query
        #   )
          return render_template("productnotfound.html")
     with open('static/data.json', "r") as file:
          data = json.load(file)
          
     filtered_data = [item for item in data if query.lower() in item['name'].lower()]

     if filtered_data:
          return render_template("results.html", results=filtered_data, query = query)
     else:
          return render_template('productnotfound.html')

@app.route("/results/")

@app.route("/results/<name>")
def results(name = None):
    return render_template(
        "results.html",
        name=name,
    )

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