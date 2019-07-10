import requests
import bs4
import csv

url = 'https://www.melon.com/chart/index.htm'
headers = {'User-Agent': ':)'}  # 우리가 누군지 정의

response = requests.get(url, headers=headers).text
# headers 없이 reponse를 print하면 406-> Not Acceptable
# # 따라서, user-agent 만들어야 됨 url 정보 뿐 아니라 headers 정보도 같이 보내기

text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50')


# print(type(rows))  # rows는 list이다. 따라서, 하나씩 가져오기

writer = csv.writer(open('melon50.csv', 'w', encoding='utf-8', newline=''))  # 대리작가 고용(writer), newline=''는 enter가 두 번 들어가므로 없애기
writer.writerow(['순위', '제목', '가수'])

for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    # print(rank, title, artist)
    writer.writerow([rank, title, artist])
