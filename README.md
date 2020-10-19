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




## heapq

> 이진  트리 기반의 최소 힙 자료구조
>
> 데이터를 정렬된 상태로 저장하기 위해서 사용
>
> PriorityQueue 와 유사
>
> [참고](https://www.daleseo.com/python-heapq/)

min heap 내의 모든 원소(k)는 항상 자식 원소들(2k+1, 2k+2) 보다 크기가 작거나 같도록 원소가 추가되고 삭제



* 모듈 임포트

  ```python
  import heapq
  ```

* 최소 힙 생성

  ```python
  heap = []
  ```

* 힙에 원소 추가

  ```python
  heapq.heappush(heap, 4)
  heapq.heappush(heap, 1)
  heapq.heappush(heap, 7)
  heapq.heappush(heap, 3)
  
  # [1, 3, 4, 7]
  ```

  가장 작은 원소가 인덱스 0에 위치

* 원소 삭제

  ```python
  heapq.heappop(heap)
  ```

* 최소값 삭제하지 않고 얻기

  ```python
  heap[0]
  ```

  인덱스 0에 가장 작은 원소가 있다고 해서, 인덱스 1에 두번째 작은 소, 인덱스 3에 세번째 작은 원소가 있다는 보장이 없음. 힙은 함수를 호출하여 원소를 삭제할 때마다 이진 트리의 재배치를 통해 매번 새로운 최소값을 인덱스 0에 위치시키기 때문

  따라서 두번째로 작은 원소를 얻으려면 반드시 heappop()을 통해 가장 작은 원소를 삭제 후에 heap[0]을 통해 새로운 최소값에 접근해야 함

* 기존 리스트를 힙으로 변환

  ```python
  heap = [4, 1, 7, 3, 8, 5]
  heapq.heapify(heap)
  print(heap)
  
  [1, 3, 5, 4, 8, 7]
  ```

  