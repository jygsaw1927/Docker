from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(servicio="usuarios", estado="ok")

@app.get("/health")
def health():
    return jsonify(status="healthy", database=os.getenv("DATABASE_URL", "").split("@")[0].split("://")[-1].split(":")[0])

@app.get("/usuarios")
def usuarios():
    return jsonify(servicio="usuarios", datos=[])
