HW 2

1. 아래 보기 중, 변경할 수 있는(mutable) 것과 변경 불가능한 것(immutable)을
    구분 하시오.
    String List Tuple Range Set Dictionary

  변경할 수 있는 것 : List, Set, Dictionary

  변경할 수 없는 것 : String, Tuple, Range

2. range와 slicing을 활용하여 1부터 50까지 숫자 중 홀수로 이루어진
    리스트를 만드시오.

  ```python
  li = list(range(1, 51))[0:50:2]
  print(li)
  ```

  

3. 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 딕셔너리를 만드시오.

dict_2ss3 = {'손현희': '28', '안유림': '25', '김은영': '25', '김은수': '26'}

