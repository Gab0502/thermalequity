from flask import Flask, render_template, jsonify

app = Flask(__name__)

BAIRROS = [
    {"nome": "Heliópolis",       "zona": "Sul",   "temp_media": 44.2, "veg_pct": 8,  "renda_media": 1200,  "risco": "crítico"},
    {"nome": "Paraisópolis",     "zona": "Oeste",  "temp_media": 45.0, "veg_pct": 6,  "renda_media": 1100,  "risco": "crítico"},
    {"nome": "Capão Redondo",    "zona": "Sul",   "temp_media": 47.4, "veg_pct": 10, "renda_media": 1400,  "risco": "crítico"},
    {"nome": "Morumbi",          "zona": "Oeste", "temp_media": 30.1, "veg_pct": 45, "renda_media": 12000, "risco": "baixo"},
    {"nome": "Alphaville",       "zona": "Oeste", "temp_media": 28.5, "veg_pct": 52, "renda_media": 18000, "risco": "baixo"},
    {"nome": "Jardins",          "zona": "Centro","temp_media": 33.2, "veg_pct": 32, "renda_media": 15000, "risco": "médio"},
    {"nome": "Itaquera",         "zona": "Leste", "temp_media": 40.1, "veg_pct": 15, "renda_media": 1800,  "risco": "alto"},
    {"nome": "Cidade Tiradentes","zona": "Leste", "temp_media": 41.8, "veg_pct": 12, "renda_media": 1500,  "risco": "alto"},
    {"nome": "Pinheiros",        "zona": "Oeste", "temp_media": 34.0, "veg_pct": 28, "renda_media": 9000,  "risco": "médio"},
    {"nome": "Vila Madalena",    "zona": "Oeste", "temp_media": 31.5, "veg_pct": 35, "renda_media": 10000, "risco": "baixo"},
]

@app.route("/")
def index():
    return render_template("index.html", bairros=BAIRROS)

@app.route("/api/bairros")
def api_bairros():
    return jsonify(BAIRROS)

@app.route("/api/bairros/<nome>")
def api_bairro(nome):
    bairro = next((b for b in BAIRROS if b["nome"].lower() == nome.lower()), None)
    if bairro:
        return jsonify(bairro)
    return jsonify({"erro": "Bairro não encontrado"}), 404

@app.route("/health")
def health():
    return jsonify({"status": "ok", "projeto": "ThermalEquity", "ods": ["ODS 10", "ODS 11", "ODS 13"]})

if __name__ == "__main__":
    app.run(debug=False)
