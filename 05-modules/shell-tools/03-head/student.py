import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file") #standaard een string === type=str)
parser.add_argument("-n", "--lines", type=int, dest="linecount")

args = parser.parse_args()
file = args.file
nlines = args.linecount

with open(file) as f:
    #python read file as array
    contents = f.readlines()
    selected_lines = contents[:nlines] #begin tot nlines
    for line in selected_lines:
        print(line, end="")