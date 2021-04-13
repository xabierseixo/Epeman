from flask import Flask
import sqlite3

basedatos = "epeman.db"

app = Flask(__name__)

@app.route("/")
def hello():
    return "Ola Mundo"
