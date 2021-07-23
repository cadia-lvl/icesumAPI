import json
import requests

def summarizer(article, summary_length= 75):
    r = requests.post("http://0.0.0.0:8080/summarizer/impl", params={'article':article, 'summary_length':summary_length})
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
    print(summarizer(data[d]['text']))
    input()
