from FFMpegService import ffmpeg_service
from OCRService import ocr_service

from flask import Flask, redirect

app = Flask(__name__)

app.register_blueprint(ffmpeg_service, url_prefix = "/ffmpeg")
app.register_blueprint(ocr_service, url_prefix = "/ocr")

@app.route('/')
def index():
    return redirect("https://ekholabs.ai", code=302)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)
