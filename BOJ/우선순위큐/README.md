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



## [절댓값 힙](https://www.acmicpc.net/problem/11286)

* 풀이

  ```python
  import sys; sys.stdin = open('11286_input.txt', 'r')
  import heapq
  
  N = int(sys.stdin.readline())
  arr = []
  for _ in range(N):
      num = int(sys.stdin.readline())
      if num != 0:
          heapq.heappush(arr, [abs(num), num])
      else:
          if arr:
              print(heapq.heappop(arr)[1])
          else:
              print(0)
  
  ```

  * 위의 문제들과 유사하게 절대값을 첫번째 원소로 넣어 작은 순서대로 arr 리스트에 저장되게 만들어서 풀이



## [가운데를 말해요](https://www.acmicpc.net/problem/1655)

* 풀이

  ```python
  import sys; sys.stdin = open('1655_input.txt', 'r')
  import heapq, sys
  
  N = int(sys.stdin.readline())
  left, right = [], []
  for _ in range(N):
      num = int(sys.stdin.readline())
      if len(left) == len(right):
          heapq.heappush(left, [-num, num])
      else:
          heapq.heappush(right, [num, num])
  
      if left and right and left[0][1] > right[0][1]:
          left_value = heapq.heappop(left)[1]
          right_value = heapq.heappop(right)[1]
          heapq.heappush(right, [left_value, left_value])
          heapq.heappush(left, [-right_value, right_value])
  
      print(left[0][1])
  
  ```

  * 중간값을 기준으로 작은 값과 큰 값을 저장하기 위한  리스트인 left, right 선언
  * 만약 두 리스트의 길이가 같다면 left에 먼저 넣게 하고(작은 값을 먼저 출력하라는 조건), 그렇지 않다면 right에 삽입
  * left에는 -를 붙여서 큰 값이 먼저 오게하고 right에는 그대로 저장해서 작은 값이 먼저 오게하여 왼쪽의 가장 큰 값과 오른쪽의 가장 작은 값을 비교할 수 있게 함
  * 두 배열이 모두 존재했을때, 왼쪽의 최대값이 오른쪽의 최소값보다 크다면 두 위치를 바꾸어 중간값을 조정하며 답을 구함