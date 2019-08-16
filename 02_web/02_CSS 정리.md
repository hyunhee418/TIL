### CSS (Cascading style sheet)

* CSS 기본 구조

```css
selector {
property-name: property-value
}
```

* 크기
  
  픽셀(pixel) - 화면을 구성하는 RGB단위
  
  * 100% : 브라우져 기본 px의 %
  
  * em : 상속받은 사이즈의 100%가 1em
  * rem : 브라우저의 기본 폰트 사이즈 1rem ( browser에 기본으로 설정되어있는 픽셀크기를 기반으로 한다. - > display 크기에 따라 달라짐.)
  * `<meta name="viewport" content="width=device-width, initial-scale=1.0">` : viewport -> 디바이스마다 화면 크기가 다름으로 인하여 상대적인 기준의 단위를 따른다.

```css
div > div {
    font-size: 0.8em;
}
```

```html
<div>
    <!-- 기본 폰트 사이즈 16px --> 
    aaaa  
    <div>
        <!-- 16 * 0.8 -->
        bbbb
        <div>
            <!-- 16 * 0.8 * 0.8 -->
            cccc
            <div>
                <!-- 16 * 0.8 * 0.8 * 0.8 -->
                dddd
            </div>
        </div>
    </div>
</div>
```



* RGBA 
  * #ffffff  16(0부터 f까지) * 16(0부터 f까지) = 256을 16진수로 표현한 것
  * 따라서, range(256)
  * (256,256,256,0)  A는 투명도
  * `opacity: 0.5` 과 같이 따로 지정 가능



* 스타일 지정 우선순위 - 내림차순

  * !important : 그러나, 되도록 쓰지 말 것
  * inline css (html 태그에 바로 스타일을 지정하는 것)
  * #id  (1, 0, 0) : 되도록 쓰지 않음, 존재 이유가 selecting을 위한 것 이므로
  * .class  <-가장 많이 쓴다 (0, 1, 0) : 가장 많이 쓰임
  * tag  <- class 다음으로 많이 쓴다  (0, 0, 1)
  * `*` -> global  (0, 0, 0)
  * browser 기본 셋팅

  

* HTML에서 스타일을 지정하는 방법 3가지

  1. 외부 스타일 시트(External Style Sheet)

     ```html
     <link rel="stylesheet" type="text/css" href="mystyle.css">
     ```

  2. 내부 스타일 시트(Internal Style Sheet)

     ```html
     <style type="text/css">
       body {font-size:9pt;}
      </style>
     ```

  3. HTML 태그 내에 스타일 지정(Inline Styles)

     ```html
     <p style="color:gray;">이 문단의 색상은 회색으로 지정됩니다.</p>
     ```

  

* 상속(selector) _ 02_selectors1을 참조하세욤,,,

```css
h1, p, a {  /* h1과 p와 a태그 모두 */
     color: red;
}

.pp {  /* class="pp" 인 것들 */
    color: orange;
}

a[href] {  /* a태그 내의 href attribute를 가진 것들 */
    color: green;
}

a[target="_blank"] {  /* a태그의 target이 "_blank"인 것들 */
    color: black;
}

h2[title~="greeting"] {  /* h2의 title에 greeting 이라는 단어를 포함하는 애들 */
    color: blueviolet;
}

div p {  /* 모든 div 안의 p 후손 요소 */
    color:chocolate;
}

div > p { /* 정확히 div 의 p 중 자식 요소 */
    color:cyan;
}

div.a {  /* div의 a클래스만 */
    
}
```



* 상속2 _ 03_selectors2를 찹조하세염

```css
body {  /* 바디 태그의 모든 요소에  */
    color: deeppink;
}

article:first-of-type {  /* article 중에 첫 번째에게 */
    background-color: red;
}

article:nth-of-type(2) {  /* article 중에 두 번째에게 */
    background-color: green;
}

article:nth-last-of-type(2) {  /* article의 마지막에서 두 번째에게 */
    background-color: blue;
}

article:last-of-type {  /* article의 마지막에게 */
    background-color: black
}

p:first-child {  /* 요소 중에 첫번째 애가 p라면 적용 */
    color: gold
}

p:last-child {  /* 요소 중에 마지막 애가 p라면 적용 */
    color: violet;
}

p:nth-child(4) {  /* 부모는 모르겠고 아무튼 4째인데 p라면 적용 */
    color: white;
}
```



* 상태에 따라 클래스를 바꾸는 가상 클래스(pseudo class selector)

```css
a {
    text-decoration: none;
    color: black;
}

a:link {  /* 방문하지 않은 link */
    color: red;
}

a:hover {  /* 마우스를 갖다댔을 때 */
    color: orange;
}

a:visited {  /* 방문한 link */
    color: beige;
}

input:focus {  /* 인풋에 포커싱이 되었을 때 */
    background-color: black;
    color: white
}
```



```css
div.rounded {
    border-radius: 30px;  - 깍는 것
    overflow: hidden;   - 부모밖으로 넘쳐흐르면 안보이게 하라.
}
```



* block 속성 < div / h1~6 / p / ol, ul, li / hr / table / form >

  * 항상 새로운 line에서 시작
  * 기본으로 width 100%를 가진다. 다른 애가 영역에 들어갈 수 없다.
  * width height margin padding 속성 지정이 가능하다
  * block 요소 안에 inline 요소를 포함 가능
  * width는 content를 지정, 전체 크기를 볼 때는 padding, border 영역도 더함.
  * 내용물이 없으면 안잡힌다.
  * div는 margin, padding, border가 기본으로 0인데
  * p는 margin이 상하 16px 이 기본

* inline 속성 

  < span / a / strong, em, del / img / br / input, select / textarea / button >

  * 새로운 라인에서 시작하지 않음, 문장 중간에 쓸 수 있다
  * content 너비만큼 가로폭을 차지한다
  * width height margin padding 속성 지정이 불가능하다
  * 상하 여백은 line height(행간)으로 지정
  * inline 요소 뒤에 공백(\n, space)이 있으면, 자동으로 4px space가 삽입
  * inline 요소 안에 block 요소 포함이 불가능하다

* inline-block 속성

  * inline의 한줄표시 + block의 margin, padding, width, height 지정 가능
  * content 너비만큼 가로폭을 가짐
  * `display: inline-block` 인 요소들 뒤에 공백은 4px space
  * 상하 여백 : margin과 line height 사용 가능
  
*  position의 default

  ​    위 => 아래, 왼 => 오

  ​    부모요소 자식요소 일 때는 부모의 위치가 기준점이 됨.

  ​    좌표값을 줘도 안먹음.

* collapse

  * `border : collapse` : 표(table)의 테두리와 셀(td)의 테두리 사이의 간격을 없앱니다. 겹치는 부분은 한 줄로 나타냅니다.
  * `visibility : collapse` : <table> 태그에서만 사용할 수 있는 값으로, 선택 테이블의 행과 열을 숨김. 하지만 여전히 투명하게 공간을 차지함.
  * table 외 사용할 경우 hidden 상태와 같다.

* display-none

  * `display: none;` : 박스가 생성되지 않고, 공간을 차지하지도 않는다.

* display

  아무것도 지정하지 않으면 parent를 따른다.

  static 하면 초기값 위치지정을 따르지 않으며, 앞에 설정된 position을 무시할 때 사용됨.

  static은 static만 상관함.

  relative 는 가까운 상위요소(부모나 바로 위의 box)를 기준으로 위치가 결정됨.

  absolute는 static인 부모는 건너뛰고, relative 만 부모 취급

  fixed는 스크롤을 내려도 붙어있음.

  sticky는 relative box를 만나기 전까지는 fixed로 따라오다가 relative 요소를 만나면 멈춤. 단, 부모 요소 중 하나라도 `overflow: hidden` 가 있다먄 보이지 않음.

  따라서, 화면 중간에 나타났다가 스크롤을 내리면 따라오는 동작에 주로 사용됨.

* `z-index: 1` : z-index는 모두 0이다. 높은 숫자를 지정해주면 우선순위화 할 수 있다. 

* Font

  폰트체

  `font-family: Arial, Helvetica, sans-serif;`

  일단 Arial로 가는데 만약에 컴퓨터에 없으면 Helvetica로 해 걔도 없으면 있을 수 밖에 없는 sans-serif로 해

  `font-style: oblique;` 

  font-style 은 normal, italic, oblique를 말함.

  `font-weight: bold;`

  font 굵기

  `letter-spacing: 5px;`

  자간

  `text-align: center;`

  정렬 -> inline 에서는 text-align으로 옮겨도 자기 안에서 가운데나 왼쪽 오른쪽 움직여봤자 차지하는 공간이 없어서 안움직임

  1. 박스에 넣어서 박스에서 움직이게 함

  `float: right`

  오른쪽으로 이동

