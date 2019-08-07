# Django

## 1. Django의 구조

M (model) : 데이터 관리

T (template) : 사용자가 보는 화면 

V (view) : 중간 관리자

유기적 존재들의 협업

1. 요청이 들어옴을 view가 인식
2. Model에게 정보를 찾아달라고 함
3. model이 database를 뒤져 view에게 줌
4. view가 template으로 보냄
5.  html로 녹여내어 내보냄

앱들이 모여서 project가 하나가 됨.

## 2. Django 시작

`pip freeze > requirements.txt`

requirements.txt 만드는 명령어

`pip install -r requirements.txt`

requirements.txt에 있는 거 다 설치해

`source ./venv/Scripts/activate`

가상환경에서 진행하겠다.

`pip install` 뒤에 버젼을 명시하지 않을 경우 가장 안정적인 버젼을 설치

`django-admin startproject 파일명` -> start



## 3. 파일

* 파일명의 project 폴더
  * master_app(파일명의 project 폴더)
  * manager.py

* 함수파일

함수 파일, url 파일을 만들어 따로 관리 -> import 로 연결

함수 파일 내 `def func(request):` request는 무조건 써야함.

* 설정파일

`INSTALLED_APPS ` 앱들의 출생신고 하는 곳

`ROOT_URLCONF` 최고 url 설정

`AUTH_PASSWORD_VALIDATORS` password 강도 설정 (보완 rule)

Internationalization => i18n

`ALLOWED_HOSTS` => 우리 프로그램이 제공될 때 접속되는 주소(이 주소로만 들어갈 수 있다.)

예를 들어 'naver.com/map'이 아닌 'map.naver.com'도 같은 페이지에 들어갈 수 있게 함.

`ALLOWED_HOSTS = ['*']` 뭐든지 다 들어와!



## 4. 앱

* 생성

`django-admin startapp pages` app 형성

settings.py에 `INSTALLED_APPS ` 에 출생신고

start 붙으면 django-admin

그 외는 python manager.py -> 매니져에게 시킴

그러나 app이 여러개가 될 경우 views가 여러 개 되어 이름이 겹치는 것이 문제가 됨.

따라서 모든 앱에 urls을 따로 둠.

urls에는 반드시 `urlpatterns = []` 를 넣어야됨. -> 기본 구조

-> 이럴 경우 project 새로 만들 때 그냥 app을 복사하고 붙여넣은 후 출생 신고하고, urls에 import include, path include넣기 때문에 구조화하기 쉬워짐.

* 실행

1. url을 쳐서 request 시작 
2. Master urls에서 'pages/'로 들어가
3. app의 pages server에서 urls에 'help/'로 들어가 
4. view.py에서 def 함수를 찾아봐 
5. templates에 help.html을 꺼내 
6. response 