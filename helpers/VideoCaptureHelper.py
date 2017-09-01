import multiprocessing
import cv2
import pytesseract as tess
import numpy as np
import requests

from PIL import Image

class VideoCapture:

    def __init__(self):
        self.seen = ''

    def process_video(self, video_url, queue, event):
        r = requests.get(video_url, stream = True)
        if(r.status_code == 200):
            byte_stream = bytes()
            for chunk in r.iter_content(chunk_size = 1024):
                byte_stream += chunk
                a = byte_stream.find(b'\xff\xd8')
                b = byte_stream.find(b'\xff\xd9')
                if a != -1 and b != -1:
                    jpg = byte_stream[a:b+2]
                    byte_stream = byte_stream[b+2:]
                    frame = cv2.imdecode(np.fromstring(jpg, dtype = np.uint8), cv2.IMREAD_COLOR)
                    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)

                    queue.put(image)
                    event.set()

    def ocr(self, queue, event):
        while True:
            event.wait()
            image = queue.get()

            array_image = Image.fromarray(image)
            txt = tess.image_to_string(array_image)
            if len(txt) > 0 and txt != self.seen:
                self.seen = txt
                with open("subs", 'a') as subsfile:
                    subsfile.write(txt)
