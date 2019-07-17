HW 1

1. Python에서사용할수없는식별자(예약어)를찾아작성하세요.

   `print`, `and`, `exec`, `not`,  `assert`, `or`, `break`, `for`, `pass`, `class`, `from`, `continue`, `global`, `raise`, `def`, `if`, `return`, `del`, `import`, `try`, `elif`, `in`, `while`, `else`, `is`, `with`, `except`, `lambda`, `yield`

2. 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다.
    (floating point rounding error)
    따라서,아래의값을비교하기위해작성해야하는코드를작성하세요.

  a = 0.1 * 3
  b = 0.3

  ``` python
  a = 0.1 * 3
  b = 0.3
  if abs(a-b) <= 1e-10:
      print('대충 같다')
  ```

  

  

3. 이스케이프 문자열 중 1)줄바꿈 2)탭 3)\을 작성하세요.

  \n , \t, \\\

4. “안녕, 철수야”를 String Interpolation을 사용하여 출력하세요.

  ```python
  name = "철수"
  print(f'\"안녕, {name}야\"')
  ```

  

5. 다음중형변환시오류가발생하는것은? 2, 5
    1) str(1)  2) int(‘30’)

  3)int(5) 4) bool(‘50’)
  5) int(‘3.5’)