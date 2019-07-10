import csv

with open('lunch.csv', 'r', encoding='utf-8') as f:  # lunch.csv를 열고 읽기전용으로 만들어 utf-8(한국어 렉 안걸리게)로 열어 f라 하겠다.
    items = csv.reader(f)
    for item in items:
        print(item)
