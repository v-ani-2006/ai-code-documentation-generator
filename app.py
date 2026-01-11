from flask import Flask, request, render_template
import os
from analyzer import analyze_code
from generator import generate_documentation

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

ALLOWED_EXTENSIONS = {'py', 'js', 'c', 'cpp', 'java', 'go'}

# Create uploads folder if not exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    if 'codefile' not in request.files:
        return "No file uploaded", 400

    file = request.files['codefile']

    if file.filename == '':
        return "No file selected", 400

    if not allowed_file(file.filename):
        return "Unsupported file type", 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    extension = file.filename.rsplit('.', 1)[1].lower()

    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()

    # ✅ Python documentation supported
    if extension == 'py':
        functions, classes, undocumented = analyze_code(code)
        docs = generate_documentation(functions, classes)

    # 🚧 Other languages – placeholder
    else:
        docs = [
            f"Documentation generation is currently supported only for Python files.\n"
            f"Support for .{extension} files will be added soon."
        ]
        undocumented = []

    return render_template(
        "result.html",
        docs=docs,
        undocumented=undocumented
    )


if __name__ == "__main__":
    app.run(debug=True)

