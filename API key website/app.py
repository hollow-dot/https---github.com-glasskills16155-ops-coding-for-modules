from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route("/home_page.html") 
def post_page():
    return render_template("/login-page")


@app.route("/login-page", methods=["GET", "POST"])

def image_submit():
    if request.method == "GET":
        return render_template(""), 400  # your page



if __name__ == "__main__":
    app.run(debug=True)