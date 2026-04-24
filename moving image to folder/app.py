from flask import Flask, render_template, request
from PIL import Image
import shutil
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = r"C:\Users\mengw\OneDrive\coding\moving image to folder\templates\images"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/succsses_page.html")
def succsses_page():
    return render_template("succsses_page.html")

@app.route("/generate", methods=["GET", "POST"]) # when to run the program 

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