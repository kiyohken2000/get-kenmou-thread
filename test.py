import requests
import json

response = requests.get('https://itest.5ch.net/subbacks/poverty.json')
res = response.json()
str = json.dumps(res)
print(str)