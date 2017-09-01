import numpy as np
import requests
import cv2
import pytesseract as tess
from PIL import Image

print("Now inside process video.")
r = requests.get("http://localhost:8090/video.mjpeg", stream = True)
if(r.status_code == 200):
    seen = ''
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

            cv2.imshow('frame', image)
            if cv2.waitKey(1) == 27:
                exit(0)
else:
    print("Received unexpected status code {}".format(r.status_code))
