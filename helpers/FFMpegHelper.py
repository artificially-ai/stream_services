from urllib.parse import urlparse, urljoin, quote

import os

import uuid
import multiprocessing
import subprocess
import re

import logging

class FFMpeg:

    def extract_stream_details(self, video_url):
        parsed_video_url = urlparse(video_url)
        path = quote(parsed_video_url.path)
        joined_url = urljoin(parsed_video_url.geturl(), path)

        ffmpeg_process = subprocess.Popen(["ffmpeg", "-i", joined_url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = ffmpeg_process.communicate()

        return self.__parse(str(err))

    def extract_subtitles(self, streams):
        parsed_video_url = urlparse(streams["videoUrl"]["url"])
        path = quote(parsed_video_url.path)
        joined_url = urljoin(parsed_video_url.geturl(), path)

        logging.info(streams)

        subtitles = []
        for details in streams["streamDetails"]:
            file_name = str(uuid.uuid4()) + ".srt"

            ffmpeg_process = subprocess.Popen(["ffmpeg", "-i", joined_url, "-map", details["id"], file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = ffmpeg_process.communicate()

            subtitles_text = ""
            with open(file_name, "r") as f:
                subtitles_text = "".join(f.readlines())
                f.close()
                subtitles.append(subtitles_text)
                os.remove(file_name)
        return "\n".join(subtitles)

    def __parse(self, output):
        regex = r"(Stream\s?.(\d.\d).?(\w+)..\s(\w+)|Stream\s?.(\d.\d).?(\(?|\w+)\s(\w+))"

        streams = []
        matches = re.finditer(regex, output)
        for matchNum, match in enumerate(matches):
            details = []
            for groupNum in range(1, len(match.groups())):
                groupNum = groupNum + 1

                if match.group(groupNum) is not None:
                    details.append(match.group(groupNum))

            stream = {"id" : details[0], "language" : details[1], "type" : details[2]}
            streams.append(stream)

        return {"streams" : streams}
