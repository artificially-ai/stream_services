# Stream Services
This repository contains WebServices used to inspect video and audio streams.

## Running with Docker

* ```docker run -d -p 8088:8088 --name=stream-services ekholabs/stream-services```

## Inspect Stream

* ```curl -X POST -v "http://localhost:8088/ffmpeg/[url_to_video_file]```
  - Sends a URL [mp4/mkv file] to the Flask WebServices to have its details extracted
