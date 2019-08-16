# 알고리즘

## 1. 배열 2

### (1) 2차원 배열

* 지그재그 순회

i % 2 짝수일때는 j가 증가는 방향

i % 2 홀수일 때 m-j-1 (m은 열의 크기) 따라서 감소방향



* 2차 배열 탐색

```python
arr = [[0...n-1], [0...n-1]]
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

for x in range(len(ary)):
    for y in range(len(ary[x])):
        for I in range(4)
        	Test X = x + dx[I]
           	Test Y = y + dy[I]
            test(any[Test X][Test Y])
```



### (2) 부분집합

& : and

| : or

^ : XOR (두 개가 다를 때만 True 같으면 False)

<< 숫자: 숫자 갯수만큼 앞으로 밀고, 나머지는 0으로 채워주기. (2진수의 경우 (X2^숫자) 한 효과)

​				주어진 크기가 있으면 앞의 값이 짤릴 수 있음.

​				부호 비트와 관련있는 경우 주의하여 작성해야 한다.

![1565762297584](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565762297584.png)

1<< n     -> 2진법으로 표현하여 bool체크

인덱스의 값을 하나씩 확인하는데 i가 점점 커지는 수를 확인하며 겹치지 않고, 확인할 수 있다.

