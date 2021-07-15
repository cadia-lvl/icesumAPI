import json
import requests

def summerizer(article, summery_length= 75):
    r = requests.post("http://0.0.0.0:8080/summarizer", params={'article':article, 'summery_length':summery_length})
    return r.text

f = open('icesum.json')

data = json.load(f)

padding = '='*10
for i,d in enumerate(data):
    for j in range(3):
        print()
    print('test nr '+str(i+1))
    print(padding+'TITLE'+padding)
    print(data[d]['title'])
    print(padding+'URL'+padding)
    print(data[d]['url'])
    print(padding+'TEXT'+padding)
    print(data[d]['text'])
    print(padding+'OUTPUT'+padding)
    print(summerizer(data[d]['text']))
    input()
