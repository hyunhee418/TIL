python은 프로젝트 하나마다 독립 가상환경을 만든다. (쓰고 있는 프로젝트만 찾기 어렵기 때문에)

pip list flask requests를 했는데

의존성으로 인해 다음과 같은 list  생성(기반이 된 코드부터 모두 불러옴)

![1562903543661](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562903543661.png)

API를 통해 단순히 받아오는 것을 넘어서 일을 시킬 수 있다.

127.0.0.1 내가 나한테 보내는 요청이므로 인터넷 렌션 필요 없음. 따라서 내가 만든 페이지는 나만 쓸 수 있음 따라서, ngrok 사용

:5000 5000번 port를 열어준다.

ngrop이랑 app.py이 계속 돌아야 하므로 cmd 로 열기



누군가 보냈을 때 