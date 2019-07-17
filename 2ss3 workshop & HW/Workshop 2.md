Workshop 2

두 개의 정수 n과 m이 주어질 때, 반복문을 사용하여 별(*) 문자를 이용해
가로의 길이가 n, 세로의 길이가 m인 사각형을 출력하시오.

```py
n = 5
m = 9

star = '*'
space = ' '
enter = '\n'

for i in range(n):
    print(star, end='')

print()

for s in range(m-2):
         print(star + space * (n - 2) + star)

for i in range(n):
    print(star, end='')
```

```python
n, m = 5, 9
for _ in range(m):
    for _ in range(n):
        print('*', end='')
    print()
```



과목명과 점수가 담긴 딕셔너리가 있을 때, 평균 점수를 출력하시오.

```pyth
student = {'python': 80, 'algorithm':99, 'django': 89, 'flask': 83}
sum = 0
n = len(list(student.keys()))
stu_values = list(student.values())
for i in stu_values:
    sum = sum + i

print(sum / n)
```

```py

student = {'python': 80, 'algorithm':99, 'django': 89, 'flask': 83}
sum(student.values()) / len(student)
```



다음은 여러 사람의 혈액형(A, B, AB, O)에 대한 데이터이다. 반복문을 사용하여
key는 혈액형의 종류, value는 인원 수인 딕셔너리를 만들고 출력하시오.

```py
blood_type = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
count_a = 0
count_b = 0
count_o = 0
count_ab = 0
dict_blood = {}


for i in blood_type:
    if i == list(set(blood_type))[0]:
        count_a += 1
        dict_blood[i] = count_a
    elif i == list(set(blood_type))[1]:
        count_b += 1
        dict_blood[i] = count_b
    elif i == list(set(blood_type))[2]:
        count_o += 1
        dict_blood[i] = count_o
    else:
        count_ab += 1
        dict_blood[i] = count_ab

print(dict_blood)
```

