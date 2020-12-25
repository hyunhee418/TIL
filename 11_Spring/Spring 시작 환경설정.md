1. JDK 설치 (java 설치 후 환경변수에 사용자변수 -> path에 자동 생성됨) 

2. cmd`java -version` 했을 때 버젼 나오는 지 확인 (나오지 않으면 path 내 자바 위치를 맨위로 올리기)

3. 시스템 변수 -> 새로만들기 -> JAVA_HOME을 jdk의 bin전 폴더로 지정 (톰캣은 java home을 보기 때문에 java home을 지정해줘야 함)

4. 이클립스 ini 파일 설정 

   -Xms, Xmx 메모리 크기 지정

5. 이클립스의 workspace 지정

6. 이클립스 실행 

7. apache-tomcat과 연결하기 위해 window -> Preferences

8. Server > Runtime Environment

9. Apache tomcat 8.0 지정

10. jre (jdk 설치된 곳) 지정

11. 환영 창 닫고 서버에서 no server를 클릭 후 new -> tomcat 버젼 지정 후 서버 생성

12. 플레이 누르면 서버 돌리기(톰캣 연동)

13. maven - 라이브러리 관리 툴