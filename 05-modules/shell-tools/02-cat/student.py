import sys

def contents(file):
    with open(file) as f:
        #python read file as string (in browser)
        return f.read()

files = sys.argv[1:]

for file in files:
    print(contents(file))