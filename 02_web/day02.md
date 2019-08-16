display 크기가 다 다르므로 절대값 단위를 쓸 수 없다.

픽셀(pixel) - 화면을 구성하는 RGB단위

em 배수 단위로 상대 단위이다.

rem browser에 기본으로 설정되어있는 픽셀크기를 기반으로 한다.

viewport 디바이스마다 화면 크기가 다름으로 인하여 상대적인 기준의 단위

우선순위

Selector Specificity: ( , , ) 더 큰수가 우선

!important> inline css >[ id(1, 0, 0) > class(0, 1, 0)] > tag(0, 0, 1) > global(0, 0, 0) > browser 기본 세팅

!important : 그러나, 되도록 쓰지 말 것

id(1, 0, 0) : 되도록 쓰지 않음, 존재 이유가 selecting을 위한 것 이므로

class(0, 1, 0) : 가장 많이 쓰임

div > p div 한단계 밑에 있는 p에만 적용

div p div의 어딘가 밑에 있는 p에 적용

p:first-child : 요소 중에 첫번째 애가 p라면 적용

p:nth-child(4) : 요소 중에 4번째 애가 p라면 적용

p:last-child: 마지막 요소가 p라면 적용
