'''from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "POST":
        username = request.form.get('fozi_b3Ar')

        if not username:
            return "Invalid username", 400 # this is error for empty box

        if username != "fozi_b3Ar":
            return render_template("index.HTML"), 401
        
        if username == "fozi_b3Ar":
            return render_template("succsses_page.HTML")


    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)'''








