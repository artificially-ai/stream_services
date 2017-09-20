from controller.FFMpegService import ffmpeg_service

from flask import Flask, redirect, jsonify, make_response

app = Flask(__name__)

app.register_blueprint(ffmpeg_service, url_prefix = "/ffmpeg")

@app.route('/')
def index():
    return redirect("https://ekholabs.ai", code=302)

@app.errorhandler(400)
def bad_request(erro):
    return make_response(jsonify({'error': 'We cannot process the file sent in the request.'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Resource no found.'}), 404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)
