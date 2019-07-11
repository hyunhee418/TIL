from iexfinance.stocks import Stock


company = Stock('TSLA', token='pk_34947d6f20564c52a9dcd62bf4d4ab5f')


print(company.get_price())


## scraping: 사람보라고 해놓은 페이지를 긁어와서 만들기
## API: dictionary 형태의 데이터를 제공받아서 그걸 분석해서 쓰기
## 패키지: 제공자가 제공하는 코드가 있어서 정보를 받을 수 있다.