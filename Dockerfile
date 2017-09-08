FROM debian:latest

RUN apt-get -y update && apt-get install -y vim procps python3-pip ffmpeg

RUN pip3 install numpy scipy pillow opencv-python pytesseract requests Flask

ADD . /ekholabs/stream_services

WORKDIR ekholabs/stream_services

ENV PYTHONPATH=$PYTHONPATH:.
ENV STREAM_SERVICES_PORT=8088
EXPOSE $STREAM_SERVICES_PORT

ENTRYPOINT ["python3"]
CMD ["app/StreamServices.py"]
