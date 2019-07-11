import datetime

from art import*
from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)


@app.route('/art')
def add():
    return render_template('art.html') 


@app.route('/result')
def result():
    input_text = request.args.get('input_text')
    font = request.args.get('font')
    result = text2art(input_text, font=font)
    return render_template('result.html', result=result)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send')  #날아온 주소부터 확인
def send():
    print(request.headers)
    return render_template('send.html')  # html에서 사용자가 입력한 정보는 여기로 온다.


@app.route('/receive', methods=['POST'])
def receive():  # requests는 사온 애 request랑 다른 애 요청에 대한 모든 정보를 담고 있다.
    
    data = request.form.get('msg')  # 요청 중 넘어온 데이터만 보여줘
    stock = Stock(data, token='pk_63c229409ff14b67a6cc81e38927f1c4').get_quote()
    company_name = stock['companyName']
    latest_price = stock['iexRealtimePrice']
    return render_template(
        'receive.html',
        c_name=company_name,
        l_price=latest_price
        )


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    return render_template('dday.html', left_days=left.days)


@app.route('/boxoffice')
def boxoffice():
    top_5 = [
        '스파이더맨 파 프롬 홈',
        '알리딘',
        '토이스토리4',
        '라이온킹',
        '이웃집 토토로'
    ]
    return render_template('boxoffice.html', movies=top_5)

if __name__ == '__main__':
    app.run(debug=True)
