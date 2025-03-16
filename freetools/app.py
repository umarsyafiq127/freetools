from flask import Flask, render_template, request, send_file
from tools.remove import remove_background
from tools.ocr import extract_text
import io

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    file = request.files["image"]
    output_image = remove_background(file.read())
    return send_file(io.BytesIO(output_image), mimetype="image/png")

@app.route("/ocr", methods=["POST"])
def ocr():
    file = request.files["image"]
    text = extract_text(file.read())
    print("OCR Output:", text)  # Tambahkan ini untuk debugging
    return render_template("ocr.html", text=text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)