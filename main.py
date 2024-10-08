from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def home():
    context = {
        "page": "home",
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return render_template("home.html", **context)

@app.route("/blog/")
def blog():
    context = {
        "page": "blog"
    }
    return render_template("blog.html",  **context)

@app.route("/about/")
def about():
    context = {
        "page": "about"
    }
    return render_template("about.html",  **context)


if __name__ == "__main__":
    app.run()