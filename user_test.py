import requests, json

url = 'http://127.0.0.1:8000/convert/'
data = {'url': 'https://youtube.com'}

r = requests.post(url, json.dumps(data))
response = r.json()
print(response)