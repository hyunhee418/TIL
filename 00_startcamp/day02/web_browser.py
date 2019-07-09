import webbrowser

urls = [
    'github',
    'google',
    'naver',
    'edu.ssafy',
    '2-ss3.slack'
]


for i in urls:
    webbrowser.open('http://' + i + '.com')
