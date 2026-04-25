from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.HTML")

def home_page():
    return render_template("home_page.HTML")


def create_post():
    return render_template("create_a_post.html")


@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "POST":
        username = request.form.get('fozi_b3Ar')

        if not username:
            return "Invalid username", 400 # this is error for empty box

        if username not in ["fozi_b3Ar", "Go4zo"]:
            return render_template("login.html"), 401
        

        return render_template("home_page.HTML")


UPLOAD_FOLDER = r"C:\Users\mengw\OneDrive\coding\moving image to folder\templates\images"


@app.route("/create-post", methods=["GET", "POST"]) # when to run the program 

def image_submit():
        if request.method == "POST": # checks bettween GET OR POST
                file = request.files.get('image')

        if not file or file.filename == "":
            return "No file uploaded", 400

        else:
         filename = secure_filename(file.filename)
    
         filepath = os.path.join(UPLOAD_FOLDER, filename)

         file.save(filepath)

         return render_template("succsses_page.html")

         return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)








