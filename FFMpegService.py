from helpers.FFMpegHelper import FFMpeg

from flask import Flask, Blueprint, jsonify, make_response, request, abort, redirect

import logging

ffmpeg_service = Blueprint('ffmpeg_service', __name__)

@ffmpeg_service.route('/<path:video_url>', methods=['POST'])
def stream_details(video_url):
    ffmpeg = FFMpeg()
    details = ffmpeg.extract_stream_details(video_url)

    return make_response(jsonify(details))

@ffmpeg_service.errorhandler(400)
def bad_request(erro):
    return make_response(jsonify({'error': 'We cannot process the file sent in the request.'}), 400)

@ffmpeg_service.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Resource no found.'}), 404)
