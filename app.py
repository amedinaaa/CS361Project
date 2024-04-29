from flask import Flask, request, render_template


app = Flask(__name__)

if __name__=="__main__":
        app.run(debug=True)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cart/")
def cart():
    return render_template("cart.html")


@app.route("/search", methods=["GET"])
def search():
     query = request.args.get("query")
     if query:
          return render_template(
               "product.html",
               name=query
          )
     else:
          return render_template("productnotfound.html")

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