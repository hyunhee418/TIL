## Bootstrap

1. Bootstrap은 무엇인가?

   - Bootstrap은 빠르고 간편한 반응형 웹 디자인(responsive web design)을 위한 open-source front-end framework이다.
   - Get start -> CSS copy head에 넣기, JS copy body 끝에 넣기

```html
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Document</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
		integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>

<body>
		<div class="alert alert-info" role="alert">
				Hello SSAFY ?!
		</div>
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
		integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
	</script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
		integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
	</script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
		integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
	</script>
</body>

</html>
```





2. Spacing (m-\*, p-\*, mx-\*, my-\* 등)

- 작성 형태 : {property}{sides} - {size}

- {property} : m(margin), p(padding)

- {sides}:  t(top), b(bottom), l(left), r(right), x(좌우), y(상하) 

  m,p 뒤에 아무것도 안적고 단독 사용시 상하좌우 모두를 의미

- size 

  - 0  => 0
  - 1 => 0.25 rem
  - 2 => 0.5 rem
  - 3 => 1 rem
  - 4 => 1.5 rem
  - 5 => 3 rem

- Examples

  ```html
      <div class="mt-3 text-right">margin top3(1rem) + Text right</div>
      <div class="mt-2 text-center">mt2(0.5rem) + Text center</div>
      <div class="mt-1 text-left">mt1(0.25rem) + Text left</div>
  
      <div class="mx-5 my-3">TEST</div>
      <div class="py-3 mx-3">TEST</div>
  ```

  

3. Colors (primary, secondary 등)

   primary - 파란색

   secondary - 회색

   success - 초록색

   danger- 빨간색

   warning - 노란색

   info - 청녹색

   light - 옅은 회색

   dark - 검정색

   white - 흰색

   transparent - 투명색

4. class="sr-only" : 시각장애인을 위한 글

5. Border

    class="border" 전체 border

   class="border-top" : bottom, right, left 도 가능

   class="border border-primary p-3" : border에 primary 색 추가

   class="m-2 rounded-circle" : margin 을 2만큼, 동그랗게 넣기

6. Display

   class="d-block"

7. 정렬

   class="text-left"

8. 대소문자

   class="text-lowercase"

9. 폰트

   class="font-weight-bold"

   class="font-weight-bold font-italic"

10. Component

    어떤 클래스들을 조합하면 마치 부품(카드, 버튼)처럼 뿅 하고 쓸수 있게 되는것들이 있는데 이런것들을 컴포넌트라고 합니다. 

    ex) `<a class="btn btn-primary" href="#" role="button">` -> a이지만 btn이 됨

    `<div class="card">` -> card

    `<div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">` ->carousel

    누르면 이동할 곳에 속성값으로 `data-toggle="modal" data-target="#lionking"`

    `<div class="modal" id="lionking" tabindex="-1" role="dialog">`

    하면 modal

    `<ul class="nav">` -> nav

    `<div class="jumbotron"> ` 점보트론 프론트 페이지, 중요페이지에서 강조할때 사용

    배경 회색 container가 없다면 width는 100%

    `<div class="alert alert-info" role="alert">
        Hello SSAFY ?!
    </div>`

    

    

11. 그리드 시스템 (Grid System)

    - 그리드 시스템은 열을 나누어 콘텐츠를 원하는 위치에 배치하는 방법을 말한다.

    - Bootstrap은 반응형 12열 그리드 시스템을 제공.

    - 그리드 레이아웃을 구성 시에는 반드시 `.row`(행)를 먼저 배치하고 행 안에 `.col-*-*`(열)을 필요한 갯수만큼 배치한다. 

      즉, container 내에> .row(행)을 먼저 배치하고 그 안에 .col-*-*(열)을 배치한다. 그리고 콘텐츠는 .col-*-* 내에 배치한다.

      container-fluid => 넓게 보고 싶을 때

    - ```html
      <div class="container bg-success p-3">
              <div class="row bg-danger"> <!-- row 먼저 배치 -->
                  <div class="col-4 border border-dark">1/3</div> <!-- col -->
                  <div class="col-4 border border-dark">1/3</div>
                  <div class="col-4 border border-dark">1/3</div>
              </div>
              <div class="row bg-primary">
                  <div class="col-9 border border-dark">
                      <div class="row">
                  <!-- 중첩하는 법 / col-9으로 3/4차지 후, 3/4를 1/3씩 배치 -->
                          <div class="col-4 border border-dark">1/3</div>
                          <div class="col-4 border border-dark">1/3</div>
                          <div class="col-4 border border-dark">1/3</div>
                      </div>
                  </div>
                  <div class="col-3 border border-dark">1/4</div>
              </div>
              <div class="row bg-warning">
                  <div class="col-9 border border-dark">3/4</div>
                  <div class="col-4 border border-dark">???</div>
                  <div class="col-6 border border-dark">???</div>
              </div>
          </div>
      ```

    - 화면의 크기에 따른 클래스 이름 및 배치

      ```html
      <article class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2 border border-light text-white">
               <p>This is Article</p>
      </article> 
      ```

      

    - |                     | Extra small <576px | Small ≥576px | Medium ≥768px | Large ≥992px | Extra large ≥1200px |
      | ------------------- | ------------------ | ------------ | ------------- | ------------ | ------------------- |
      | Max container width | None (auto)        | 540px        | 720px         | 960px        | 1140px              |
      | Class prefix        | `.col-`            | `.col-sm-`   | `.col-md-`    | `.col-lg-`   | `.col-xl-`          |
      | # of columns        | 12                 |              |               |              |                     |

    - col offset

      : offset은 중앙정렬시 또는 비우고 시작하고 싶을 때 사용한다.

      ```html
      <section class="row bg-secondary">
                  <article class="col-6 offset-3 border border-white">
                      <p>This is Article</p>
                  </article>
                  <article class="col-4 offset-4 border border-white">
                      <p>This is Article</p>
                  </article>
              </section>
      ```

      



- 사용 가능한 클래스
  - container
  - border
  - text
- 사용 가능한 컴포넌트 (Components) 
  - jumbotron
  - nav
  - card
  - carousel
  - btn ( button )