import zipfile
import sys

filename = sys.argv[1]

with zipfile.ZipFile(filename, 'r') as myzip:
    #pass #doe niks
    for file in myzip.namelist():
        print(file)
    #of
    #print("\n".join(myzip.namelist())) alles op nieuwe lijn
