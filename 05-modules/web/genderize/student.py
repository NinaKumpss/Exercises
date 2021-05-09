import sys
import urllib.request
import json
import argparse

name = sys.argv[1]
parser = argparse.ArgumentParser()
parser.add_argument('name')
args = parser.parse_args()

basis_url = 'https://api.genderize.io'

with urllib.request.urlopen(f'{basis_url}/?name={args.name}') as f:
    data = f.read().decode('utf-8')
    data = json.loads(data)
   
    gender = data['gender']
    prob = round(data['probability'] * 100)
    print(f'{gender} ({prob}%)')

#print(name)