from helpers.VideoCaptureHelper import VideoCapture

from flask import Flask, Blueprint, jsonify, make_response, request, abort, redirect, send_file
from PIL import Image

import logging
import multiprocessing
import cv2
import requests
import pytesseract as tess

ocr_service = Blueprint('ocr_service', __name__)

@ocr_service.route('/<path:video_url>', methods=['POST'])
def ocr_video(video_url):
    try:
        video_url = request.view_args['video_url']

        cap = VideoCapture()

        queue_capture = multiprocessing.Queue(1)
        event_capture = multiprocessing.Event()

        video_p = multiprocessing.Process(target=cap.process_video, args=(video_url, queue_capture, event_capture))
        ocr_p = multiprocessing.Process(target=cap.ocr, args=(queue_capture, event_capture))

        try:
            video_p.start()
            ocr_p.start()

            video_p.join()
            ocr_p.join()
        except KeyboardInterrupt:
            video_p.terminate()
            ocr_p.terminate()

        return "OK"
    except Exception as err:
        logging.error('An error has occurred whilst processing the file: "{0}"'.format(err))
        abort(400)

@ocr_service.errorhandler(400)
def bad_request(erro):
    return make_response(jsonify({'error': 'We cannot process the file sent in the request.'}), 400)

@ocr_service.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Resource no found.'}), 404)
