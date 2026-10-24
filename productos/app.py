from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(servicio="productos", estado="ok")

@app.get("/health")
def health():
    return jsonify(status="healthy", database=os.getenv("DATABASE_URL", "").split("@")[0].split("://")[-1].split(":")[0])

@app.get("/productos")
def productos():
    return jsonify(servicio="productos", datos=[])
