# import random # 필통꺼낸다

# random.choice([1, 2, 3, 4, 5]) #필통에서 연필꺼낸다

# from random import choice #서랍 속 필통에서 연필만 꺼낸다.

# choice([1, 2, 3, 4, 5])

from flask import Flask, render_template  # render_template: template를 보여주는 함수
import random


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  # 무조건 template 파일에서 찾음


@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return str(lucky)


# @app.route('/get_lotto/<int:num>')
# def get_lotto():


@app.route('/hello/<name>')  # variable routing
def hello(name):
    return f'hi, {name}'


@app.route('/pick_lunch/<int:count>')  # variable routing
def c(count):
    menus = [
        '짜장면',
        '짬뽕',
        '탕수육',
        '볶음밥',
        '유산슬',
        '깐쇼새우'
    ]
    picks = random.sample(menus, count)
    return str(picks)  # 숫자는 못나가므로 str으로 바꿔서 내보내기


@app.route('/cube/<int:number>')
def cube(number):
    return str(number ** 3)


if __name__ == '__main__':
    app.run(debug=True)
