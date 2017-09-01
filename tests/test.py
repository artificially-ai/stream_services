import multiprocessing
import subprocess
import re

p = subprocess.Popen(["ffmpeg", "-i", "http://localhost:8000/Guardians%20of%20the%20Galaxy%20Vol.%202.2017.BDRip.H.264.720p.NNMCLUB.mkv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = p.communicate()

regex = r"Stream\s?.\d?.\d?.\w+..\s\w+"

matches = re.finditer(regex, str(err))
for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

regex = r"[a-zA-Z]\D[a-zA-Z]+\b"

test_str = "Stream #0:0(eng): Video"

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

regex = r"\d.\d"

test_str = "Stream #0:0(eng): Video"

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
