# n = '0DEC'
n = '0269FAC9A0'
password = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']
def Bbit_print(i):
    global response
    for s in range(3, -1, -1):
        response += '1' if i & (1<<s) else '0'

response = ''
for i in n:
    if ord(i) - ord('A') >= 0:
        Bbit_print(ord(i) - ord('A')+10)
    else:
        Bbit_print(int(i))

res = 5
while res < len(response):
    if response[res] == '1':
        if response[res-5:res+1] in password:
            print(password.index(response[res-5:res+1]), end=' ')
            res += 5
    res+= 1