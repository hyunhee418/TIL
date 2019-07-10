from iexfinance.stocks import Stock

company = Stock('TSLA', token='pk_34947d6f20564c52a9dcd62bf4d4ab5f')

print(company.get_price())


## scraping: 사람보라고 해놓은 페이지를 긁어와서 만들기
## API: dictionary 형태의 데이터를 제공해서 그걸 쓰기
## 패키징: 웹에 짜여진 코드가 있어서 정보를 긁어올 수 있다.