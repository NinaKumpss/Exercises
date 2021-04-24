import urllib.request
import json
from PIL import Image
import sys 

if len(sys.argv) == 1:
    url = f"http://xkcd.com/info.0.json"
else:
    id = int(sys.argv[1])
    url = f"http://xkcd.com/{id}/info.0.json"

with urllib.request.urlopen(url) as input:
    data = input.read().decode('utf-8')
    jsonData =json.loads(data)
    with urllib.request.urlopen(jsonData['img']) as image:
        Image.open(image).show()
