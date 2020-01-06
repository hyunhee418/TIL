import requests
import bs4


url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80/'
response = requests.get(url).text
#url에서 data 가져오기
text = bs4.BeautifulSoup(response, 'html.parser')
#Python에서 select_one을 쓸 수 있게 하는 함수, data를 예쁘게 만들어서 알아볼 수 있게 함.
# print(text)
dust = text.select_one('#main_pack > div.content_search.section._atmospheric_environment > div > div.contents03_sub > div > div > div.main_box > div.detail_box > div.tb_scroll > table > tbody').text.replace('   ', ', ')
# t1 = dust.select_one('span.lv2').text


#데이터에서 필요한 정보만 추출
print(dust)
# print(t1)
