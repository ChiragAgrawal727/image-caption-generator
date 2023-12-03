import os
from flask import Flask, render_template, request, redirect, url_for
from caption_generator import caption_generator
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static\\uploads'
app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)
            caption = caption_generator(image_path)
            return render_template('result.html', image_path=image_path, caption=caption)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
