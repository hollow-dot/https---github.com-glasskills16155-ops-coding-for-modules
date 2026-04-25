from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("test_page.html")


@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "POST":
        username = request.form.get('fozi_b3Ar')