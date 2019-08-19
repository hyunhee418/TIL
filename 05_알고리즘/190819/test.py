s = 'Reverse this strings'
v = [0]*len(s)
s = s[::-1]
print(s)

for i in range(len(s)):
    v[i] = s[len(s)-i-1]
print(''.join(v))

c = 9312456
n = 1

while c // (10 ** n) != 0:
    n += 1
for s in range(n-1, 0, -1):
    print(chr(ord('0') + (c // (10 ** s))), end='')
    c = c % (10 ** s)
print(chr(ord('0') + (c % 10)),end='')

