import requests
# from requests import post

print(requests)
url = 'http://13.125.222.176/quiz/jordan'
headers = {'Accept' : 'application/json', 'Content-Type': 'application/json'}
data={'nickname': '서울4반손현희', 'yourAnswer': 'kubernetes'}
res = requests.post(url, json=data, headers=headers)
a = res.json()
print('--------')
print(a)