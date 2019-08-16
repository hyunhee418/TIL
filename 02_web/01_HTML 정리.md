### 웹 서비스

웹 서비스 - 서버 컴퓨터에서 제공하는 무언가

url로 요청을 보내고, 정보를 얻음 ex) requests 모듈, postman

- 요청의 종류
  1. 줘라 (HTML 문서)
     - server - 요청을 받고 분석하여 일을 하고, 해당하는 것을 준다.
  2. 받아라 (로그인, 회원가입 등)
     - 사람이 처리요청 데이터를 넘기고, 자동화된 프로그램이 응답해준다.
     - url 요청이 들어오면 일을 끝내고 html을 보낸다.

**<u>우리는 서버컴퓨터에서 요청과 응답을 처리할 프로그램을 개발한다.</u>** 

탐색기와 browser는 같은 일을 한다.

- 탐색기 -> file:// (내컴퓨터) 위치
- Browser -> http:// (남의 컴퓨터) 주소

Web의 변화

- Static web - Sever는 file을 들고 있고, 정확한 요청을 해야 file을 줌(도서관과 같음). 단순하다는 장점이 있다.
- Dynamic web web application program (Web APP) - Program이 돌아 분석하고, 일해서 문서(html)를 보냄.

URI -> URL(Uniform Resource Locator, 파일 식별자)는 네트워크 상에서 자원이 어디 있는 지를 알려주기 위한 고유 규약이다.

1. HTML이란 무엇인가?
   Hyper Text Markup Language

   웹페이지를 작성하기 위한 역할 표시 언어

   최종적으로 나가게 되는 정보

   

   참고용어

   * HTTP(hyper text transfer protocol)(s - secure) 

   * CSS : Cascading Style Sheet

   * IP : 8비트(0-255)의 숫자로 구성된 숫자 집합, 각자가 갖고있는 주소의 개념

   * 도메인 : 네트워크상의 컴퓨터를 식별하는 호스트명

   * URL : 도메인 + 경로, 실제 해당 서버가 저장된 자료의 위치

   * W3C - 웹 표준을 만든 곳

2. 시멘틱태그

   컨택츠의 의미를 설명하는 태그로서, HTML 5에 새롭게 추가된 태그이다.

   `header`, `nav`, `aside`, `section`, ` article`, `footer`

3. HTML 문서 기본 구조

   ```html
   <!DOCTYPE html>   --> HTML 문서다 선언
   <html lang="ko">  --> 대표언어
   <head>            --> 문서 제목, 코드(인코딩)와 같이 해당 문서의 정보를 담고 있음.
   					  브라우져에 나타나지 않으며, meta 태그 선언이 이루어지는 곳.
   	<meta charset="UTF-8">
   -->컴퓨터가 문자열 쓸 때 따르는 표준법>> 종종 한국어가 깨지는 경우도 있다.
       <meta name="viewport" content="width=device-width, initial-scale=1.0">     --> 화면을 잡을 때 우리가 접속한 browser 크기로 잡는다. 접속된 가로 크기로 쓰자.
   	<title> Document </title>
   </head>
   <body>			  --> 브라우져 화면에 나타나는 정보로 실제 내용에 해당됨.
   </body>
   </html>
   ```

   참고 용어

   * `<meta>` : 정보의 정보

4. 요소 (태그 + 내용)

   요소는 태그와 내용 `<h1> </h1>` ->여닫기

   * tag 전체를 element
* 태그 안에 내용을 content
   * attribute속성
* attribute-value 속성값
  

Self-closing element : 닫는 태그가 없는 태그 

​										대표적으로 img `<img src="url"/>` -> 태그 내부에서 스스로 닫기

   속성 : 태그 다음에 나오는 것 `<a href="#">` 에서 href는 속성

   DOM 트리 -> 태그 중첩사용 

   ```html
   <body>						-->body태그와 h1태그는 부모 자식 관계
       <H1>웹문서</H1>
       <Ul>					-->h1태그와 ul태그는 형제 관계
        <li>HTML</li>		-->li태그끼리 형제관계
           <li>CSS</li>
    </Ul>
   </body>
   ```

   

   h1 : 가장 중요한 제목. 따라서, 여러 개를 쓸 수 없다. 글씨를 조절하고 싶다면 CSS에서 조절하는 것

​	-> 글을 구조화할 때 content가 갖고 있는 역할 지정만 생각하고, 스타일은 나중에 함.

​		`<li style="list-style-type: circle"></li>`

​	-> none, square, circle, lower-alpha, upper-alpha, upper-roman

* 수업시간 태그 정리

  `<b></b>` : <b>bold</b>

  `<strong></strong>` : <strong>strong</strong>

  `<i></i>` : <i>italic</i>

  `<em></em>` : <em>em</em>

  `<mark></mark>` : <mark>mark</mark>

  `<del></del> ` : <del>del</del>

  `<ins></ins> ` : <ins>ins</ins>

  `<br>` : 띄어쓰기, 정말 필요할 때만 쓰기

  `<span></span>` :글쓰는 중에 가운데 내용만 어떻게 스타일을 다르게 하고 싶을 때 

  `<hr>` : 가로선을 그음 전환이 일어나는 느낌을 갖도록 하는 역할

  `<pre></pre>` : 태그 사이에 쓰는 내용은 그대로 파일에 나감(띄어쓰기 가능).  자유롭게 사용 							가능. 

  `<q></q>` : 인용문구 " 내용" inline

  `<blockquote></blockquote>` : 긴 인용구 띄어쓰기 내용 띄어쓰기 - block

  `<img src="#" alt="설명">` : height, width 지정해주면 적용가능하지만, CSS에서 하자. 

  alt=이 이미지가 뭔지 설명 안쓴다고 에러나진 않지만, 인터넷으로 인해 이미지가 안올 때 뭔지 알려주거나 시각장애인분들이 들을 수 있는 것.

  `<a href="#"></a>` : 링크, 속성 중 target="_blank" 이용하면 새창으로 열기.
  
   href=자원이 어디있는지만 써주면 됨.
  
  `<iframe src="#"></iframe>` : 우리 문서에 다른 html 문서를 넣음 
  
  ```html
  <table border="1px solid black">  <!-- 속성과 속성 사이에 띄어쓰기 -->
  		<tr>    					  --> 가로줄 시작
  			<th></th> 				  --> 세로 제목
  			<th>월</th>
  			<th>화</th>
  			<th>수</th>
  		</tr>
  		<tr>
  			<td>A 코스</td>			 --> 세로 내용 채우기
  			<td rowspan="2">짬뽕</td>  --> rowpan="2" 세로 줄 2개 먹을래
  			<td colspan="2">초밥</td>  --> colspan="2" 가로 줄 2개 먹을래
  		</tr>
  		<tr>						  --> 위에서 세로 줄 합쳐서 여기는 3개만 씀 
			<td>B 코스</td>
  			<td>김치찌개</td>
			<td>삼계탕</td>
  		</tr>
	</table>
  ```
  
  ![1565498600537](C:\Users\son\AppData\Roaming\Typora\typora-user-images\1565498600537.png)
  
  `<form action=""></form>` : action에 있는 url 주소로 내용을 전송해주세요.
  
  

`<select name="menu" id="">  						   --> select랑 option은 짝꿍
  	<option value="a"> 내용 </option>
    <option value="b" selected> 내용 </option>  --> 얘로 골라져 있기
      <option value="c" disable> 내용 </option>	  --> 얘는 있지만 못골라
</select>`

  ```
박스를 누르면 option에 있는 애들을 고를 수 있다.
  
  `<input type="checkbox" name="option" value="a" >`내용:  글씨 옆에 체크할 수 있는 애 만들기 (네모) 한 번 더 누르면 체크를 없앨 수 있음 disabled, checked 사용 가능 !
  
  `<input type="radio" name="a">` 내용 : 글씨 옆에 체크할 수 있는 애 만들기(동그라미) 네임을 모두 같은 애로 하면 1개만 선택할 수 있다. 네임을 다르게 하면 다시 눌러도 체크를 없앨 수 없다. disabled, checked 사용 가능 
  
  `<textarea name="" id="" cols="30" rows="10"></textarea>` : text 길게 쓰는 input.`
  
  
  ```