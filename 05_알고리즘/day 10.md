# 알고리즘 응용

## 비트 연산

2's complement 

1의 보수를 해주면 0이 1로 모두 바뀌고, 1이 0으로 모두 바뀜

2의 보수는 1의 보수에 +1을 해줌

**음수의 경우는 원래 수에서 1의 보수로 만든 후 +1을 하여 2의 보수로 만들어줌**



XOR 연산을 통해 값의 변화를 확인



## 실수

부동 소수점

소수점 앞에는 하나의 정수만 나오게 옮겨줌

자리수를 왔다갔다 할까봐 지정

* 단정도 실수(32비트) : 실수의 유효 자릿수들을 부호화된 고정 소수점으로 표현

  지수부가 8비트이므로 0(01111111)을 기준으로 -되는 반은 음수, +되는 반은 양수로 사용

* 배정도 실수(64비트) : 실제 소수점의 위치를 지수 승으로 표현

표현할 수 있는 수의 범위와 오차도 배정도 실수가 더 좋다.