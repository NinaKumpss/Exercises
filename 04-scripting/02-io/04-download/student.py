import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1], 'r') as input:
    contents = input.read()
    print(contents)