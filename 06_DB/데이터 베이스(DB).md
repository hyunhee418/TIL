## 데이터 베이스(DB)

체계화된 데이터의 모임

몇 개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 구조화하여 기억시켜 놓은 자료 집합체

### 데이터 베이스 장점

1. 데이터 중복 최소화
2. 데이터 무결성
   * 정확한 정보를 보장
3. 데이터 일관성
4. 데이터 독립성
   * 물리적 독립성과 논리적 독립성

5. 데이터 표준화
6. 데이터 보안 유지

### RDBMS (관계형 데이터베이스 관리 시스템)

Create

Retrieve

Update

Delete

DB는 프로그램이다. 프로그램을 연결하여 프로그램을 동작하는 것

### SQLite

관계형 데이터베이스 관리 시스템의 데이터를 관리하기 위한 특수 목적의 프로그래밍 언어

구글 안드로이드 운영체제에 기본적 탑재된 데이터베이스

임베디드 소프트웨어에서 활용

간단한 DB구성 가능, 오픈소스 프로젝트

테이블, 스키마를 정의하는 명령어 -> CREATE DRPO ALTER

테이블 삽입 (INSERT)

데이터 갱신(UPDATE)

삭제 (DELETE)

검색 (SELECT)



* 베이터 베이스 생성 : 

`sqlite3 tutorial.sqlite3`

`.mode csv`

`import 파일이름.csv 테이블이름`



* 테이블 모든 데이터 보기

`SELECT * FROM 테이블이름;`



* 테이블 모든 데이터 이쁘게 보기

`.header on`

`.mode column`

`SELECT * FROM 테이블이름;`



* 몇개의 column만 보기

`SELECT column1, column2 FROM 테이블이름;`



* 데이터 몇 개만 보기

`SELECT * FROM 테이블 이름 LIMIT 10;`



* 특정 위치에서 몇개만 가져오기

`SELECT * FROM 테이블이름 LIMIT 10 OFFSET 3;`



* 특정값만 가져오기

`SELECT * FROM 테이블이름 WHERE column1=value;`



* 테이블에서 특정 column값을 중복없이 가져오기

`SELECT DISTINCT colum FROM 테이블이름;`

ex)

`SELECT DISTINCT age FROM classmates;`



* SELECT 에서 평균값

ex) users에서 30 이상인 사람의 계좌 평균 잔액

`SELECT AVG(column) FROM users WHERE age >= 30;`



* SELECT에서 개수

ex) 지역번호가 02인 사람 수

` SELECT * FROM count(users) WHERE phone LIKE '02-%';`



* Like

  '-' 반드시 이 자리에 한 개의 문자 존재

  '%' 이 자리에 문자가 있을 수도 없을 수도

ex)이름이 '준'으로 끝나는 사람만

` SELECT  phone, age FROM users WHERE first_name LIKE '%준';`

ex)중간 번호가 5114인 사람은?

`SELECT first_name FROM users WHERE phone LIKE '_%-5114-_%';`



* ORDER BY 앞에 있는 조건을 먼저 정렬하고 그 중에 다음 조건을 정렬

  ASC : 오름차순

  DESC : 내림차순

`SELECT age, last_name FROM users ORDER BY last_name, age LIMIT 10;`



* 데이터 삭제

`DELETE FROM 테이블이름 WHERE column1=value1;`



* 데이터 수정

`UPDATE 테이블이름 SET colum1=value1, colum2=value2 WHERE column1 = value1`



* 테이블 생성

```CREATE TABLE 테이블이름 (
CREATE TABLE 테이블이름 (
	column1 datatype PRIMARY KEY AUTOINCREMENT,
	column2 datatype,
	...)
```

​	AUTOINCREMENT는 자동적으로 늘어나는 값 그러나 내부적으로 CPU, 메모리, 디스크 공간을 추가로 불필요하게 사용하므로 엄격히 필요하지 않을 경우 사용을 피하기



* 테이블 명 변경

`ALTER TABLE 현재 이름 RENAME TO 바꿀 이름`



* 새로운 컬럼 추가

`ALTER TABLE 테이블 이름 ADD COLUMN 컬럼이름 datatype;`

NOT NULL 할꺼면 DEFAULT 넣기

`ALTER TABLE 테이블 이름 ADD COLUMN 컬럼이름 datatype DEFAULT 1;`



DB 내 여러 테이블 존재

SQLite은동적데이터타입으로,기본적으로유연하게데이터가들어간다. BOOLEAN은없으며정수0,1으로저장된다.



* 테이블 조회

`.tables`



* Schema 조회

`.shema 테이블이름`



* 테이블 삭제

`DROP TABLE 테이블이름`



* Data 추가

`INSERT INTO 테이블이름(column1, column2...) VALUES 값(value1, value2...);`

NOT NULL 을 붙이면 무조건 써야됨

전체 값을 넣을 때는 column이름을 굳이 넣지 않아도 됨

### 스키마(shema)

데이터 베이스에서 자료의 구조, 표현방법, 관계를 정의한 구조

| column | datatype |
| ------ | -------- |
| id     | INT      |
| age    | INT      |
| phone  | TEXT     |
| email  | TEXT     |

### 테이블(Table)

열과 행으로 조직된 데이터 요소들의 집합

### 열(column), 행(row), PK(기본키 primary key: INT만 가능)



* orm

`User.objects.all()`

- sql

`SELECT * FROM users_user;`



- orm

``` 
User.objects.create(first_name='길동',                    
                    last_name='홍', 
                    age=30, 
                    country='제주특별자치도', 
                    phone='010-1234-1234',
                    balance=300)
```

```
user = User()
user.first_name = '길동'
..
user.save()
```

```
INSERT INTO users_user
VALUES ('길동', '홍', 30, '제주', '010-1234-1234', 300);
```



해당 user 레코드 조회

* orm

```
User.objects.get(pk=101)
```

- sql

```
SELECT * FROM users_user
WHERE id=101;
```



해당 user 레코드 수정

* orm

```
user = User.objects.get(pk=101)
user.last_name = '김'
user.save()
```



- sql

```
UPDATE users_user
SET last_name='김'
WHERE id=101;
```



해당 user 레코드 삭제

* orm

`User.objects.get(pk=101).delete()`

```
user = User.objects.get(pk=101)

user.delete()

```

- sql

```
DELETE FROM users_user
WHERE id=101;
```



조건에 따른 쿼리문

1. 전체 인원수

* orm

`User.objects.all().count()`

- sql

`SELECT COUNT(*) FROM users_user;`

2. 나이가 30인 사람의 이름

* orm

`User.objects.filter(age=30).values('first_name')`

<QuerySet [{'first_name': '영환'}, {'first_name': '보람'}, {'first_name': '은영'}]>

print(User.objects.filter(age=30).values('first_name').query)

`SELECT "users_user"."first_name" FROM "users_user" WHERE "users_user"."age" = 30`

- sql

`SELECT first_name FROM users_user WHERE age=30;`



나이가 30이상인 사람의 인원 수

__gte : 이상

__gt : 초과

__lte : 이하

__lt: 미만

* orm

`User.objects.filter(age__gte=30).count()
print(User.objects.filter(age__gte=30).query)`

query는 queryset의 인스턴스 변수로 존재함.

`SELECT "users_user"."id", "users_user"."first_name", "users_user"."last_name", "users_user"."age", "users_user"."country", "users_user"."phone", "users_user"."balance" FROM "users_user" WHERE "users_user"."age" >= 30`

* splite

`SELECT COUNT(*) FROM users_user
WHERE age >= 30;`



나이가 30이면서 성이 김씨인 사람의 인원 수

* orm

`User.objects.filter(age=30, last_name='김').count()`

`User.objects.filter(age=30).filter(last_name='김')`

`print(User.objects.filter(age=30).filter(last_name='김').query)`

`SELECT "users_user"."id", "users_user"."first_name", "users_user"."last_name", "users_user"."age", "users_user"."country", "users_user"."phone", "users_user"."balance" FROM "users_user" WHERE ("users_user"."age" = 30 AND "users_user"."last_name" = 김)`

* sql

`SELECT COUNT(*) FROM users_user
WHERE age=30 AND last_name='김';`




지역번호가 02인 사람의 인원 수

LIKE
exact, contains, startswith, endswith
iexact, icontains, istartswith, iendswith
i -> case insensitive (대소문자 무시)

* orm

`User.objects.filter(phone__startswith='02-').count()`

- sql

`SELECT COUNT(*) FROM users_user
WHERE phone LIKE '02-%';`




거주 지역이 강원도이면서 성이 황씨인 사람의 이름
* orm

`User.objects.filter(country='강원도', last_name='황').values('first_name')`

- sql

`SELECT first_name FROM users_user
WHERE last_name='황' AND country='강원도';`



정렬 및 LIMIT, OFFSET


나이가 많은 사람 10명
* orm

age를 내림차순으로 정렬해서 10개

`User.objects.order_by('-age')[:10]`
`print(User.objects.order_by('-age')[:10].query)`

`SELECT "users_user"."id", "users_user"."first_name", "users_user"."last_name", "users_user"."age", "users_user"."country", "users_user"."phone", "users_user"."balance" FROM "users_user" ORDER BY "users_user"."age" DESC  LIMIT 10`

- sql

`SELECT * FROM users_user
ORDER BY age DESC LIMIT 10;`




잔액이 적은 사람 10명
* orm

balance를 오름차순

`User.objects.order_by('balance')[:10]`

- sql

`SELECT * FROM users_user
ORDER BY balance ASC LIMIT 10;`



성, 이름 내림차순 순으로 5번째 있는 사람

* orm

`User.objects.order_by('-last_name', '-first_name')[4]`

- sql

`SELECT * FROM users_user
ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 4;`



표현식

관련 문서



전체 평균 나이
* orm

`from django.db.models import Avg
User.objects.aggregate(Avg('age'))`

{'age__avg': 28.23}

- sql

`SELECT AVG(age) FROM users_user;`


김씨의 평균 나이
* orm

`from django.db.models import Avg
User.objects.filter(last_name='김').aggregate(Avg('age'))`

- sql

`SELECT AVG(age) FROM users_user
WHERE last_name='김';`



계좌 잔액이 가장 높은 값

* orm

`from django.db.models import Max
User.objects.aggregate(Max('balance'))`

- sql

`SELECT MAX(balance) FROM users_user;`



계좌 잔액 총액

* orm

`from django.db.models import Sum
User.objects.aggregate(Sum('balance'))`

- sql

`SELECT SUM(balance) FROM users_user;`

