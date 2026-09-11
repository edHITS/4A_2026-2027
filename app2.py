from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop2.db"
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Product {self.login}>"

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    products = db.session.scalars(db.select(Product).order_by(Product.login)).all()
    request.args.get("is_available")
    return render_template("list.html", products=products)

@app.route("/element/<int:id>")
def element(id):
    product = db.get_or_404(Product, id)
    return render_template("element.html", product=product)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        age_val = request.form.get("age")
        p = Product(
            login=request.form["login"],
            password=request.form["password"],
            age=int(age_val) if age_val and age_val.strip() else None,
            available="available" in request.form
        )
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    p = db.get_or_404(Product, id)
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    p = db.get_or_404(Product, id)

    if request.method == "POST":
        age_val = request.form.get("age")
        p.login = request.form["login"]
        p.password = request.form["password"]
        p.age = int(age_val) if age_val and age_val.strip() else None
        p.available = "available" in request.form

        db.session.commit()
        return redirect(url_for("element", id=p.id))

    return render_template("edit.html", p=p)

if __name__ == "__main__":
    app.run(debug=True)