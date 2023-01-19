from flask import Flask, render_template, request
from pdf_compress import compress_pdf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    # Do something with the uploaded file (compress, save, etc.)
    return "File uploaded and compressed!"

if __name__ == '__main__':
    app.run(debug=True)
