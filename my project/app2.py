from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("passwor_username.html")


@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "POST":
        username = request.form.get('fozi_b3Ar')
        password = request.form.get('password')
        if not username or not password:
            return render_template("passwor_username.html"), 400 # this is error for empty box
          
        if username == "fozi_b3Ar" and password == "fozi_b3Ar":
            return render_template("succsses_page.HTML")
        
    return render_template("passwor_username.html")
if __name__ == "__main__":
    app.run(debug=True)