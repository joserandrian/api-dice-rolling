# wsgi.py
import random
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({ 'rool': random.randint(1, 6)})
   

        