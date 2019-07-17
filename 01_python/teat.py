# users 안의 id 와 password 는 바꿔도 상관 없습니다.
users = [
    {'id': 'john', 'password': 'qwer1234'},
    {'id': 'neo', 'password': '12341234'},
    {'id': 'jason', 'password': 'kingjason'},
]

id_1 = input('id를 입력하세요:  ')

for i in range(len(users)):
    if id_1 != users[i]['id']:
        print('존재하지 않는 사용자입니다.')
        break
    else:
        pw_1 = input('password 를 입력하세요:  ')
        
        if users[i]['password'] == pw_1:
            print('환영합니다!')
        else:
            print('패스워드가 올바르지 않습니다.')
        break
