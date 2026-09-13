from flask import Flask, render_template, request, redirect, url_for
from models import db
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sklep.db"
db.init_app(app)

class Produkt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), nullable=False)
    cena = db.Column(db.Float, nullable=False)
    dostepny = db.Column(db.Boolean, default=True)
    def __repr__(self):
        return f"<Produkt {self.nazwa}>"
with app.app_context():
    db.create_all()

@app.route("/")
def lista():
    produkty = Produkt.query.all()
    return render_template("lista.html", produkty=produkty)
@app.route("/produkt/<int:id>")
def szczegoly(id):
    p = Produkt.query.get_or_404(id)
    return render_template("produkt.html", p=p)
@app.route("/dodaj", methods=["GET", "POST"])
def dodaj():
    if request.method == "POST":
        p = Produkt(nazwa=request.form["nazwa"],
        cena=float(request.form["cena"]))
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("lista"))
    return render_template("dodaj.html")
@app.route("/usun/<int:id>", methods=["POST"])
def usun(id):
    p = Produkt.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for("lista"))

if __name__ == "__main__":
    app.run(debug=True)