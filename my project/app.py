from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "POST":
        username = request.form.get('fozi_b3Ar')

        if not username:
            return "Invalid username", 400

        return f"Hello, {username}!"
    
    return "Go back and submit the form."

if __name__ == "__main__":
    app.run(debug=True)






