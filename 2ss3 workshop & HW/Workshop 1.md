Workshop 1

두개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.



```py
n = 5
m = 9

star = '*'
space = ' '
enter = '\n'

print(star * n + enter + (m - 2) * (star + space * (n -2) + star + enter) + star * n)
```



```
n, m = 5, 9
print((('*' * n) + '\n') * (m-1) + '*' * n)
print('end')
```



print 함수를 한번만 사용하여 다음 문장을 출력하시오.

`print('\"파일은 C:\\Window\\User\\내문서\\Python에 저장되어 있습니다.\"\n 나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'')`



다음과 같은 이차방정식이 있을 때 근을 찾는 수식을 파이썬 코드를 이용하여 출력해보시오.

```python
a = 1
b = 4
c = -21
x1 = (-b + (((b * b) - (4 * a * c)) ** (1 / 2))) / 2*a
x2 = (-b - (((b * b) - (4 * a * c)) ** (1 / 2))) / 2*a
print(x1, x2)
```

