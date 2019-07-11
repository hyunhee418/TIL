dynamic web - 능동적으로 요청에 대해 어떤 행동을 하여 정보를 보냄

static web - 문서에서 파일을 여는 방식

start bootstrap - portfolio가져오기 좋은 곳





app.py로 정보가 날아옴

날아온 주소 확인

주소 찾기 (/send)다

그러면 send.html로 가자.



html에서 뭔가를 입력하여 버튼을 누르자 양식이 /receive로 넘어감

app.py에서 요청이 날아오니

주소 찾기

주소의 코딩에서 사용자가 보낸 정보 중에 어떤 정보를 쓸까

정보(name)를 찾아 같이 실어서 receive.html로 보내기

receive. html을 띄우자!!!



name 서버에서 요청이 들어오면 찾기 위해 있는 아이

class selector를 위해 사용 class가 ''인 애를 잡아줘 명령시 

`.code{ color: blue; }`

class가 code인 애는 다 파란색으로 해줘

id = 같은 이름을 갖을 수 없다. 문서전체에서 1개만 존재 selector

`#secret{ color : yello; }`

id가 secret인 애들은 다 노랑으로 해줘



server는 요청하면 들어주는 애

내가 보내는 데이터가 받아주는 서버 입장에서 database를 건들때 즉, 중요할 때 안전해야될 때 POST를 쓴다. (url이 뒤가 삭제되어 나가기 때문에)