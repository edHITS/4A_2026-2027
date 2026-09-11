from flask import Flask, render_template, abort

app = Flask(__name__)

# Lista 5 słowników (pola: id, nazwa, kategoria, cena, dostepny - logiczne)
PRODUKTY = [
    {"id": 1, "nazwa": "Laptop", "kategoria": "Komputery", "cena": 2999, "dostepny": True},
    {"id": 2, "nazwa": "Mysz", "kategoria": "Akcesoria", "cena": 49, "dostepny": False},
    {"id": 3, "nazwa": "Klawiatura", "kategoria": "Akcesoria", "cena": 199, "dostepny": True},
    {"id": 4, "nazwa": "Monitor", "kategoria": "Ekrany", "cena": 899, "dostepny": False},
    {"id": 5, "nazwa": "Słuchawki", "kategoria": "Audio", "cena": 250, "dostepny": True},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lista")
def lista():
    return render_template("produkty.html", produkty=PRODUKTY)

@app.route("/element/<int:id>")
def element(id):
    produkt = next((p for p in PRODUKTY if p["id"] == id), None)
    if produkt is None:
        abort(404)

    return render_template("element.html", produkt=produkt)


if __name__ == "__main__":
    app.run(debug=True)
