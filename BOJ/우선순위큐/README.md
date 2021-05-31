# [우선수위 큐 문제 풀이](https://www.acmicpc.net/step/13)

> heapq 활용

* 기본 형태

  ```python
  import heapq
  
  # 기본 활용
  arr = []
  heapq.heappush(arr, num)
  heapq.heappop(arr)
  
  board = [1, 2, 3, 4, 5]
  heapq.heapify(board)
  
  # 가장 
  ```

* 기본적으로 우선순위가 가장 큰 원소가 첫 번째 인덱스에 위치
* 하지만 두 번째가 두 번째로 큰 것은 아님
* pop하면 우선순위가 가장 큰 원소가 출력되면 제거됨
* 다음으로 우선순위가 큰 원소가 첫 번째 인덱스로 오면서 다시 배열 됨
* 숫자의 경우에는 기본적으로 내림차순이기 때문에 가장 작은 수부터 출력
* 가장 큰 수 부터 출력하기 위해서는 heapq에 저장할 때, [-num, num]과 같이 음수를 붙인 숫자를 첫 번째 원소로 하는 리스트 자료형태로 저장



## [최대힙](https://www.acmicpc.net/problem/11279)

* 풀이

  ```python
  import sys; sys.stdin = open('11279_input.txt', 'r')
  import heapq
  
  N = int(sys.stdin.readline())
  arr = []
  for _ in range(N):
      num = int(sys.stdin.readline())
      if num > 0:
          heapq.heappush(arr, [-num, num])
      else:
          if arr:
              print(heapq.heappop(arr)[1])
          else:
              print(0)
  
  ```

  * int(input())으로 풀이하게 된다면 시간 초과가 뜨기 때문에 sys.stdin.readline()으로 풀이
  * heapq에 기존의 숫자만 입력하여 풀이하면 최소값부터 출력되기 때문에 [-num, num]과 같은 형태로 저장하여 가장 큰 숫자가 앞으로 올 수 있도록 만들어 풀이



## [최소힙](https://www.acmicpc.net/problem/1927)

* 풀이

  ```python
  import sys; sys.stdin = open('1927_input.txt', 'r')
  import heapq
  
  N = int(sys.stdin.readline())
  arr = []
  for _ in range(N):
      num = int(sys.stdin.readline())
      if num > 0:
          heapq.heappush(arr, num)
      else:
          if arr:
              print(heapq.heappop(arr))
          else:
              print(0)
  
  ```

  * 최대힙 문제와 반대로 heapq 배열에 원래의 숫자를 입력하여 가장 작은 숫자대로 출력할 수 있도록 만듦

