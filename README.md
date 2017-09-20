# Stream Services
This repository contains WebServices used to inspect video and audio streams.

## Running with Docker

* ```docker run -d -p 8088:8088 --name=stream-services ekholabs/stream-services```

## Inspect Stream

* ```curl -H "Content-Type: application/json" -X POST -v -d '{"url" : "URL_TO_VIDEO"}' http://localhost:8088/ffmpeg/streamDetails```
  - Sends a URL [mp4/mkv/avi file] to the Flask WebServices to have its details extracted
