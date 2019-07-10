import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text
data = json.loads(response)  # 현재 data는 'dictionary data'로 되어있기 때문에 str으로 읽고 있음. 따라서, ''를 없애기 위한 함수 json 이용
print(data['bnusNo'])

real_numbers = []
for key, value in data.items():  # dictionary에서 key, value 같이 꺼내기
    if 'drwtNo' in key:
        real_numbers.append(value)

print(real_numbers)