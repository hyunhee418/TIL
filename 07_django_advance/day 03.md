# Django

## Relational database(관계형 데이터베이스)

### 1. 1: N

일정 Data1개에 (Article 1개)에 여러 줄의 데이터 table을 추가할 때 (model 2개 table 2개, table 내 model_id column 추가)

ex) 댓글

### 2. 1:1

일정 Data1개에 (Article 1개)에 한 줄의 데이터 table을 추가할 때 (model 2개 table 2개, table 내 model_id column 추가)

ex) 회원가입 상세정보 입력

### 3. N: N

연결 table이 필요 (model 2개 table 3개)

'1번 모델이 2번 모델이랑 연결되어있다.

1번 모델이 3번 모델이랑 연결되어있다.'

는 정보 table과 같다.

ex) 수강신청



## Model Form

* ArticleModelForm - 유효성 검사

* Model - 저장만 하는 곳

한 세트로 생각하기

`$ python manage.py migrate board zero`

table 없애기