from flask import render_template

from app import app


@app.route("/") # Регистрация урла / на нашем сайте (http://127.0.0.1:5000/)
def home():
    return render_template(
        "home/home2.html"
    )
