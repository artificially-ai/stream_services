from urllib.parse import urlparse, urljoin, quote

import multiprocessing
import subprocess
import re

class FFMpeg:

    def extract_stream_details(self, video_url):
        parsed_video_url = urlparse(video_url)
        path = quote(parsed_video_url.path)
        joined_url = urljoin(parsed_video_url.geturl(), path)

        ffmpeg_process = subprocess.Popen(["ffmpeg", "-i", joined_url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = ffmpeg_process.communicate()

        stream_details = []
        streams = self.__parse(str(err))
        for stream in streams:
            typ = (self.__parse(stream, regex = r"[a-zA-Z]\D[a-zA-Z]+\b"))
            track = (self.__parse(stream, regex = r"\d.\d"))
            stream_details.append({"type" : typ , "track" : track})

        return stream_details

    def __parse(self, output, regex = r"Stream\s?.\d?.\d?.\w+..\s\w+"):
        result = []
        matches = re.finditer(regex, output)
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1

            result.append(match.group())

        return result
