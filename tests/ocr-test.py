import multiprocessing
import cv2
import pytesseract as tess
from PIL import Image

def process_video(queue, event):
    cap = cv2.VideoCapture("/Users/wilderrodrigues/Documents/dl_subs.mp4")

    next_frame = cap.get(cv2.CAP_PROP_FPS)
    _ , frame = cap.read()
    while frame is not None:
        cap.set(cv2.CAP_PROP_POS_FRAMES, next_frame)
        next_frame += cap.get(cv2.CAP_PROP_FPS)

        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)

        queue.put(image)
        event.set()

        _ , frame = cap.read()

def ocr(queue, event):

    while True:
        event.wait()
        image = queue.get()

        array_image = Image.fromarray(image)
        txt = tess.image_to_string(array_image)
        if len(txt) > 0:
            with open("subs", 'a') as subsfile:
                subsfile.write(txt)

if __name__ == '__main__':
    logger = multiprocessing.log_to_stderr()
    logger.setLevel(multiprocessing.SUBDEBUG)

    queue_capture = multiprocessing.Queue(1)
    event_capture = multiprocessing.Event()

    video_p = multiprocessing.Process(target=process_video, args=(queue_capture, event_capture))
    ocr_p = multiprocessing.Process(target=ocr, args=(queue_capture, event_capture))

    try:
        video_p.start()
        ocr_p.start()

        video_p.join()
        ocr_p.join()
    except KeyboardInterrupt:
        video_p.terminate()
        ocr_p.terminate()
