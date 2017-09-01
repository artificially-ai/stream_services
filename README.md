# Stream Services
This repository contains WebServices used to inspect video and audio streams.

## Start FFMPEG

* ```ffserver -d -f ./config/ffserver.conf```
  - Starts a FFMPEG server on port 8090.

## Video Streaming

* ```ffmpeg -threads 2 -stream_loop -1 -re -i [path_to_mp4_file] http://localhost:8090/video.ffm```
  - Streams the input MP4 file to the FFMPEG video feed.

## Start WebService

* ```python3 StreamServices.py```
  - Starts a Python Flask application on port 8088.

## OCR

* [wip]

## Extract Stream Details

* ```curl -X POST -v "http://localhost:8088/ffmpeg/[url_to_video_file]```
  - Sends a URL [mp4 file] to the Flask WebServices to have its details extracted
  - This step depends only on the WebService. No need to have the FFMPEG Video Streaming services running.

Remark: this is still work in progress. The code will be pulled and more information will be made available.
