# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# We don't add app.run() here because Vercel will handle that in a serverless manner
