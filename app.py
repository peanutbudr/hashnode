from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Pass the current year or any data you want into the template
    return render_template("index.html", current_year=datetime.now().year)

if __name__ == "__main__":
    app.run(debug=True)
