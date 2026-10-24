from flask import Flask, jsonify
import os
import sqlite3

app = Flask(__name__)
DB = os.getenv("SQLITE_PATH", "/data/pedidos.sqlite3")

@app.before_request
def initialize_database():
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    with sqlite3.connect(DB) as connection:
        connection.execute("CREATE TABLE IF NOT EXISTS pedidos (id INTEGER PRIMARY KEY AUTOINCREMENT)")

@app.get("/")
def index():
    return jsonify(servicio="pedidos", estado="ok")

@app.get("/health")
def health():
    return jsonify(status="healthy", database="sqlite")

@app.get("/pedidos")
def pedidos():
    return jsonify(servicio="pedidos", datos=[])
