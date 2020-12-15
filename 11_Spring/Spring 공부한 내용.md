# Spring 

## 구성파일과 역할 

pom.xml > 메이븐에서 필요한 라이브러리 관리

web.xml > 기본환경설정(서블릿 위치, encoding, spring controller, welcome-file 등)

action-servlet.xml > Mapping (spring에서 제공하는 라이브러리 : jsp파일 위치, json파일 사용예정 등)



## Process flow

**기본**

url -요청 > web.xml -응답> index.jsp



**요청사항**

url > web.xml > 서블릿 -요청> controller -응답> 서블릿 > jsp파일 > page나오기



**DB 요청사항**

url > web.xml > 서블릿 > controller > 서비스 > 서비스imple > Dao -요청> DB -응답> Dao > 서비스imple > 서비스 > controller > 서블릿 > jsp파일 > page나오기



## 기타

### 서비스를 사용하는 이유

Dao는 단순 Data를 가져오는 역할만 진행하므로 서비스단에서 Controller가 용이하게 DB를 사용할 수 있도록 비지니스 로직을 처리한다.

MVC 패턴의 핵심은 View는 자신이 요청할 Controller만 알고있으면 되고, Controller는 화면에서 넘어오는 매개변수들을 이용해 Service 객체를 호출하는 역할을 한다. Service 는 불필요하게 Http 통신을 위한 HttpServlet을 상속 받을 필요도 없는 순수한 자바 객체로 구성된다(그렇기에 Service 에 request나 response와 같은 객체를 매개변수로 받아선 안된다. 그걸 사용해야하는 작업은 컨트롤러에서 해야한다.). 그렇기에 자신을 어떤 컨트롤러가 호출하든 상관없이 필요한 매개변수만 준다면 자신의 비즈니스로직을 처리하게된다. 즉 모듈화를 통해 어디서든 재사용이 가능한 클래스파일이라는 뜻이다.



### 서비스imple 사용하는 이유

서비스를 모듈화함으로써 어디서든 재사용이 가능한 클래스파일이 된다. Service는 view에 종속적인 코드가 없기때문에 그대로 재사용 할 수 있으며 추가적인 요청사항이 들어오면 기존 소스를 수정하는게 아니라 기존 service 인터페이스를 구현한 다른 클래스를 구현해 그 객체를 사용하게끔 할 수 있다. OCP에 입각한 변화에는 닫혀있고 확장에는 열려있는 구조로 만들 수 있는 것이다.비즈니스 로직을 처리하는 모델은 요청사항에 따라 언제든 변할수있는 부분이었고 변화에 대응하기위해 확장을 염두하여 인터페이스로 구성했던것이다.