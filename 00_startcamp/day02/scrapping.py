import requests
import bs4


url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
#url에서 data 가져오기
text = bs4.BeautifulSoup(response, 'html.parser')
#Python에서 select_one을 쓸 수 있게 하는 함수, data를 예쁘게 만들어서 알아볼 수 있게 함.
exchange_rate = text.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
#데이터에서 필요한 정보만 추출

print(exchange_rate.text)
