# 알고리즘

## 리스트

### 순차리스트

배열을 기반으로 구현된 리스트

삭제하였을 때 빈 공간이 발생

빈 공간을 없애고자 이동시키면 그에 따른 연산이 발생

따라서 작업 성능이 떨어지고, 메모리 낭비가 발생한다.

### 연결리스트

메모리의 동적할당을 기반으로 구현된 리스트

자료의 논리적인 순서와 메모리 상의 물리적인 순서가 일치하지 않고, 개별적으로 위치하고 있는 원소의 주소를 연결하여 하나의 전체 자료구조를 이룸

메모리 낭비가 없고, 성능이 좋다.

* 노드

  (1) 데이터 필드

  원소 값을 저장하는 자료구조

  저장할 원소의 종류가 많으면 여기에 저장

  (2) 링크 필드

  다음 노드의 주소를 저장하는 자료구조

* 헤드

  링크드 리스트의 처음 주소

* Null

  더이상 연결된 것이 없다.

```python
def addtoFirst(data):
	global Head
	Head = Node(data, Head)    # 주소값만 넣어주기
    
def add(pre, data):
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)
 
def addtoLast(data):  # 마지막에 데이터 삽입
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None:  # 마지막 노드 찾을 때까지
            p = p.link
        p.link = Node(data, None)
        
def delete(pre):  # 삭제
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link
```

#### 이중 연결 리스트의 삽입 연산

A의 연결을 끊는 것 먼저 진행할 경우 B의 값을 찾아갈 수 없으므로, D에 B의 주소를 삽입하는 것이 제일 먼저

그 다음 A에 D의 주소를 저장

이 후, D에 A 주소를 저장하여 A와 연결한다.

마지막으로 B에 D의 주소를 저장

#### 이중 연결 리스트의 삭제 연산

A에 C의 주소를 연결

C에 A주소 연결

### 삽입 정렬

데이터의 개수가 작을 때는 삽입, 많을 때는 병합 정렬

순차리스트를 사용하면 버블 소트와 유사. 자리 바꿀 때 모두 밀고, 당기고 다시 정렬해야하므로 비효율적이다.

링크드 리스트를 사용할 경우 주소값만 바꿔주면 되므로 순차리스트보다 효율적이다.

병합정렬은 최악의 경우에도 nlogn만큼의 시간복잡도

퀵소트보다 훨씬 성능을 높일 수 있다.