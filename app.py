from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hendryk"
@app.route("/o-nas")
def o_nas():
    return "Zdane INF.03"
@app.route("/kontakt")
def kontakt():
    return "Napisz e-mail na: hbulak@zstil.pl"

@app.route("/regulamin")
def regulamin():
    return "1. Pełna kulturka"

@app.route("/admin")
def admin():
    return "<h1>Brak dostępu</h1>", 403

@app.route("/api/info")
def info():
    return {"nazwa": "APP TEST", "autor": "Hendryk", "wersja": "0.0.1"}

if __name__ == "__main__":
    app.run(debug=True)