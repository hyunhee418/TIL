# 알고리즘

## 1. Intro

: (사전적 의미) <b>유한한</b> 단계를 통해 문제를 해결해나가기 위한 절차나 방법

주로 컴퓨터용어로 쓰이며, 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법    -> 어떤 문제를 해결하기 위한 절차



* 슈더코드 -> 의사코드라고 쓰이기도 함. 언어적으로 완벽하게 구현된 코드가 아닌 알고리즘을 설명하기 위한 코드. 문법적으로 보다는 어떻게 돌아갈지만 보여주기. 

  *순서도로 표현했을 때 길어지면 오히려 복잡해짐. 오류를 찾기 힘듬.* -> 긴 코드일수록 슈더코드가 보기 쉬움.



* 좋은 알고리즘

1. 정확성

2. 작업량 : 연산의 횟수를 적게.

3. 메모리 사용량 : 적은 메모리. 그러나, 요즘엔 크게 문제가 되지 않음.

4. 단순성

5. 최적성

   

* 시간 복잡도(Time Complexity)

실제 걸리는 시간을 측정보다는 실행되는 명령문의 개수를 계산하는 방법을 사용 -> 실제 시간은 변수가 너무 많으므로

​			* 표현법 (같은 의미로 생각하기)

​			0(n) 빅오 : 입력데이터의 갯수 n제곱

​			오메가(n)

​			세타(n)



빅오 : 가장 큰 영향을 주는 n에 대한 항만 표시 

차수가 가장 수만, 계수는 생략하여 표시



## 2. 배열

C, Java는 배열 내 다른 type이 들어갈 수 없지만, Python의 container data type은 배열 내 다른 type이 들어갈 수 있다. -> 객체지향언어이니까

C, Java는 메모리, 크기를 계산해야하지만, python의 container data type는 크기를 가변적으로 사용 가능

그러나, 느려지기 때문에 append없이 애초에 li 내 모두 넣고 index로 꺼내기



* 배열의 필요성

프로그램 내 여러 개의 변수를 하나의 선언을 통해 사용하도록 함.

단순히 다수의 변수 선언을 의미하는 것이 아니라, 다수의 변수로는 하기 힘든 작업을 배열을 통해 쉽게 할 수 있음.



* 1차원 배열의 선언

언어 : Compiler 방식의 언어, Interprinter 방식의 언어



Interprinter 언어는 compile 과정이 없이 바로 실행하여 결과를 보여줌. 실행결과를 바로 볼 수 있음. 그러나 속도가 많이 늦음. python은 대용량 데이터를 고려해서 설계됨. ex) Basic, Python

 Compiler방식의 언어는 compile하고, link 하는 과정이 있다. compile하여 object 코드를 통해 (.exe, .dll 파일을 만들고, 사용자가 운영체제로 실행시킴.) compile 중 최적화 해줌. 따라서, 실행시간이 빠름. ex) C, C++, Java

Script 언어: 특정 목적을 위해 만들어진 언어. Java script 언어: 웹브라우져를 위해 만들어진 언어



### (1) 완전 검색(Exaustive Search)

생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법

Brute-force / generate-and-test 기법이라고도 불린다.

모든 경우의 수를 테스트하고, 최종 해답 도출

일반적으로 경우의 수가 상대적으로 작을 때 유용하다.

모든 경우의 수를 생성하고 테스트하여 수행속도는 느리지만, 정확도는 높아짐.

순열 : 순차적으로 나열하여 n개 나열하면  nPr = n* (n-1)* ... (n-r+1)

### (2) 탐욕적 알고리즘

여러 경우 중에 최적이라고 생각하는 것을 선택하고, 또 다시 최적을 선택하는 형식으로 최종답을 도달

지역적 최적으로 최종답을 만들었다고 하여 그것이 최적이라는 보장은 없음.

### (3) 정렬

특정 기준에 의해 작은 값부터 큰 값(오름차순) 혹은 그 반대(내림차순)의 순서대로 재배열하는 것

키 : 자료를 정렬하는 기준이 되는 특정 값

* 대표적인 정렬 방식의 종류

  * 버블 정렬 -> 가장 기초가 되지만 실제 적용하지 않음 시간복잡도가 O(n*2)이 나오므로

    ​				  	상대적으로 비교교환 횟수가 적음

    ​					  인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

    ​					   

  * 카운팅 정렬 -> 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개 씩 있는 지 세는 작업을 하여 선형 시간에 정렬하는 효율적 알고리즘

    단, 정수나 정수로 표현할 수 있는 자료에 대해서만 적용가능 : 각 항목의 발생 회수를 기록하기 위해 정수 항목을 인데스 되는 카운트의 배열을 사용하기 때문

    카운트들을 위한 충분한 공간할당을 위해 집합 내 가장 큰 정수를 알아내야함.

    특수한 경우에 유용하게 사용가능

  * 선택 정렬

  * 퀵 정렬

  * 삽입 정렬

  * 병합 정렬