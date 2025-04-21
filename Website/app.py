from flask import Flask, render_template, request, redirect, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER_PDF = 'static/pdfs'
UPLOAD_FOLDER_COVER = 'static/covers'

# Crear carpetas si no existen
os.makedirs(UPLOAD_FOLDER_PDF, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_COVER, exist_ok=True)

# Lista de libros (puedes reemplazar con SQLite si quieres)
books = []


@app.route('/')
def index():
    return render_template('index.html', books=books)


@app.route('/upload', methods=['POST'])
def upload():
    title = request.form['title']
    pdf = request.files['pdf']
    cover = request.files['cover']

    pdf_filename = pdf.filename
    cover_filename = cover.filename

    pdf.save(os.path.join(UPLOAD_FOLDER_PDF, pdf_filename))
    cover.save(os.path.join(UPLOAD_FOLDER_COVER, cover_filename))

    books.append({
        'title': title,
        'pdf': pdf_filename,
        'cover': cover_filename
    })

    return redirect('/')


@app.route('/pdfs/<filename>')
def download_pdf(filename):
    return send_from_directory(UPLOAD_FOLDER_PDF, filename)


if __name__ == '__main__':
    app.run(debug=True)
