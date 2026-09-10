from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return ("<h1>Lista tras:</h1>"
            "<ul>"
            "<li><a href='/czesc/Admin/17'>Imie i wiek</a>"
            "<li><a href='/kalkulator'>Kalkulator</a>"
            "<li><a href='/tabliczka/3'>Tabliczka mnożenia</a>"
            "<li><a href='/produkty?kat=owoce&sort=15&nazwa=japko'>Produkty</a>"
            "<li><a href='/baza/1'>Baza</a>"
            "<li><a href='/start'>Przekierowanie</a>"
            "</ul>")
@app.route("/czesc/<imie>/<int:wiek>")
def czesc(imie, wiek):
    return f"Cześć, {imie}, masz {wiek} lat!"

@app.route("/kalkulator")
def kalkulator():
    return ("<h5><a href='/'>Wróć</a></h5>"
            "<h1>Kalkulator</h1>"
            "<ul>"
            "<li><a href='/dodaj/2/2'>Dodawanie</a>"
            "<li><a href='/odejmij/2/2'>Odejmowanie</a>"
            "<li><a href='/pomnoz/2/2'>Mnożenie</a>"
            "<li><a href='/podziel/2/2'>Dzielenie</a>"
            "<li><a href='/potega/2/2'>Potęgowanie</a>"
             "</ul>")
@app.route("/dodaj/<int:a>/<int:b>")
def dodaj(a,b):
    return f"Wynik dodawania {a} + {b} = {a + b}"

@app.route("/odejmij/<int:a>/<int:b>")
def odejmij(a,b):
    return f"Wynik odejmowania {a} - {b} = {a - b}"

@app.route("/pomnoz/<int:a>/<int:b>")
def pomnoz(a,b):
    return f"Wynik mnożenia {a} * {b} = {a * b}"

@app.route("/podziel/<int:a>/<int:b>")
def podziel(a,b):
    return f"Wynik dzielenia {a} : {b} = {a / b}"

@app.route("/potega/<int:a>/<int:b>")
def potega(a,b):
    return f"Wynik potęgowania {a} do potęgi {b} = {a ** b}"

@app.route("/tabliczka/<int:n>")
def tabliczka(n):
    if n> 20:
        return "Za duży zakres", 400
    text = ''
    for i in range(1, n+1):
        for j in range(1, n+1):
            text += f"{i} * {j} = {i*j}<br>"
    return f"{text}"

@app.route("/produkty")
def produkty():
    kat = request.args.get("kat")
    sort = request.args.get("sort", type=int)
    nazwa = request.args.get("nazwa")
    return f"Kategoria: {kat}, Sortowanie: {sort}, nazwa: {nazwa}"

@app.route("/baza/<int:id>")
def baza(id):
    baza = {1: "produkty", 2: "tabliczka", 3: "kalkulator", 4: "czesc"}
    return baza[id]

@app.route("/start")
def start():
    return redirect(url_for("produkty"))

@app.route("/api/info")
def info():
    return {"nazwa": "APP TEST", "autor": "Hendryk", "wersja": "0.0.1"}

if __name__ == "__main__":
    app.run(debug=True)