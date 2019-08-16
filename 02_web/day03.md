Box 특징

1. box를 무조건 가로를 다 먹으려고 함.

   따라서, 영역 안에 다른 애가 들어갈 수 없다.

2. content : 내용, padding : 여유공간, margin : 다른 요소와의 거리

3. 내용물이 없으면 안잡힌다.

width는 content를 지정 전체 크기를 볼 때는 padding, border 영역도 더함.





block 속성  

div/ h1 ~ h6/ p/ ol, ul ,li/ hr/ table/ form



특징

항상 새로운 line 에서 시작

기본으로 wiidth 100%

width height margin padding 속성 지정 가능

block 

요소 안에 inline 요소를 포함 가능



inline 속성

span/ a/ strong, em, del/ img/ br/ input, select/ textarea/ button



특징

새로운 라인에서 시작하지 않으며, 문장 중간에 쓸 수 있다.

content 너비만큼 가로폭을 차지한다.

width height margin padding 속성 지정 불가능. 상하 여백은 행간으로 지정

inline 요소 뒤에 공백(\n, space)이 있으면, 자동으로 space(4px)가 들어감

inline 요소 안에 block 요소 포함 불가능



inline-block 속성

inline의 한줄표시 + block의 margin, padding, width, height

content 너비만큼이 기본 가로폭

display: inline-block인 요소들 뒤에 공백은 space(4px)

상하 여백: margin과 line height로 가능



 position의 default

​    위 => 아래, 왼 => 오

​    부모요소 자식요소 일 때는 부모의 위치가 기준점이 됨.

​    좌표값을 줘도 안먹음.



width, height는 상속되진 않지만, parent의 크기에 제한되어 max가 parent 크기

absolute는 부모가 무조건 static이 아니여야 함.

absolute는 부모가 static 이면 부모를 건너뛰어 body 기준으로 움직임. 부모가 relative면 부모기준으로 움직임.



z-index는 모두 0이다. 높은 숫자를 지정해주면 우선순위화 할 수 있다.



.sans-serif{

​    font-family: Arial, Helvetica, sans-serif;

}

일단 얘로 가는데 만약에 컴퓨터에 없으면 얘(2번째)로 해 걔도 없으면 있을 수 밖에 없는 3번째로 해



inline 에서는 text-align으로 옮겨도 자기 안에서 가운데나 왼쪽 오른쪽 움직여봤자 차지하는 공간이 없어서 안움직임

1. 박스에 넣어서 박스에서 움직이게 함

   