import json
import requests
import string
import random

def gen_rand(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def summerizer(article, summery_length= 11):
    r = requests.post("http://0.0.0.0:8080/summarizer/impl", params={'article':article, 'summary_length':summery_length})
    return r.text

sum_length = 10

for i in range(0,20):
    print("sum length:", sum_length, " i:", i)
    response = summerizer(gen_rand(i), sum_length)
    print(i, response)


