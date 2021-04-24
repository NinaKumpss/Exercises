import sys
import urllib.request
import json
import re

artist = "%20".join(sys.argv[1].split())
title = "%20".join(sys.argv[2].split())
url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
print(url)

with urllib.request.urlopen(url) as input:
    jsonData =json.loads(input.read())
    print(jsonData[lyrics])