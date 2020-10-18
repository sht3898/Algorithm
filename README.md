# 알고리즘 문제

## 중요 함수

## lambda

> lambda 인자: 표현식

* 예시

* 두 수를 더하는 함수

  ```python
  def hap(x, y):
      return x + y
  ```

* 람다로 표현하면

  ```python
  (lambda x, y: x+y)(10, 20)
  ```



## map

> map(함수, 리스트)

* 예시

  ```python
  list(map(lambda x: x**2, range(5)))
  [0, 1, 4, 9, 16]
  ```




## enumerate

> 인덱스와 원소 값을 동시에 반환

* 예시

  ```python
  for idx, num in enumerate(numbers):
      print(idx, num)
  ```

  