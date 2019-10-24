# RESTfull URI

```
GET           https://localhost:500/articles/1
HTTP VERB          HOST NAME        RESOURCE ID
```



1. URI (통합된 자원 식별자) 자원을 나타내는 유일한 주소
2. 자원(명사)만을 표현
3. HTTP method 로 자원을 조작

| HTTP method | URI         | Description         |
| ----------- | ----------- | ------------------- |
| GET         | /articles   | article 목록        |
| GET         | /articles/1 | id = 1 article 상세 |
| POST        | /articles   | article 생성        |
| PATCH       | /articles/1 | id = 1 article 수정 |
| DELETE      | /articles/1 | id = 1 article 삭제 |



dump data로 추출한 데이터를 load data로 입력 (fixtures)



$ pip freeze > requirements.txt

$ pip install -r requirements.txt

