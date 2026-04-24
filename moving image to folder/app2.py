from flask import request
from werkzeug.utils import secure_filename
import os

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        file = request.files['image']
        
        if file.filename != '':
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            file.save(filepath)  # 👈 this "moves" the image into your folder
            
            return "Image uploaded!"

    return '''
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="image">
      <button type="submit">Upload</button>
    </form>
    '''