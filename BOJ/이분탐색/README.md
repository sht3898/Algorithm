# 이분(이진) 탐색 문제풀이(Binary Search)

> 기본구조

* 재귀함수 구현

  ```python
  def binary_search(array, target, start, end):
      if start > end:
          return None
      mid = (start + end) // 2
      # 찾은 경우 중간점 인덱스 반환
      if array[mid] == target:
          return mid
      # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
      elif array[mid] > target:
          return binary_search(array, target, start, mid-1)
      # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
      else:
          return binary_search(array, target, mid+1, end)
  ```

  

* 반복문 구현

  ```python
  def binary_search(array, target, start, end):
      while start <= end:
          mid = (start + end) // 2
          # 찾은 경우 중간점 인덱스 반환
          if array[mid] == target:
              return mid
         	# 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
          elif array[mid] > target:
              end = mid - 1
          # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
          else:
              start = mid + 1
  	return None
  ```

  

## [수 찾기](https://www.acmicpc.net/problem/1920)

* 풀이

  ```python
  import sys
  sys.stdin = open('1920_input.txt', 'r')
  
  N = int(input())
  board = list(map(int, input().split()))
  board.sort()
  M = int(input())
  for num in list(map(int, input().split())):
      start, end = 0, len(board) - 1
      check = 0
      while start <= end:
          mid = (start + end) // 2
          if num == board[mid]:
              check = 1
              break
          elif board[mid] > num:
              end = mid - 1
          else:
              start = mid + 1
      print(check)
  
  ```

  * 기본적인 이분탐색 풀이방법으로 해결



## [나무 자르기](https://www.acmicpc.net/problem/2805)

* Python3, Pypy3 모두 통과 풀이

  ```python
  import sys
  sys.stdin = open('2805_input.txt', 'r')
  
  N, M = map(int, input().split())
  board = list(map(int, input().split()))
  start = 1
  end = max(board)
  while start <= end:
      mid = (start + end)//2
      total = sum(b-mid for b in board if b > mid)
      if total >= M:
          start = mid + 1
      else:
          end = mid - 1
  print(end)
  
  ```

  * 범위를 탐색하며 자른 나무의 길이의 합이 M보다 크면 탐색 시작 범위를 mid+1로 옮기고 작거나 같으면 탐색 종료 범위를 mid-1로 옮겨서 계속 탐색
  * total 부분을 구할 때 한번에 구하니 해결이 되었다

* Pypy3만 통과 풀이

  ```python
  import sys
  sys.stdin = open('2805_input.txt', 'r')
  
  N, M = map(int, input().split())
  board = list(map(int, input().split()))
  start = 1
  end = max(board)
  while start <= end:
      mid = (start + end)//2
      total = 0
      for b in board:
          if b-mid > 0:
              total += b-mid
      if total >= M:
          start = mid + 1
      else:
          end = mid - 1
  print(end)
  
  ```

  

## [숫자카드2](https://www.acmicpc.net/problem/10816)

* 딕셔너리 활용 풀이

  ```python
  import sys; sys.stdin = open('10816_input.txt', 'r')
  
  N = int(sys.stdin.readline())
  board = list(map(int, sys.stdin.readline().split()))
  M = int(input())
  arr = list(map(int, sys.stdin.readline().split()))
  dic = {}
  for num in board:
      if num in dic:
          dic[num] += 1
      else:
          dic[num] = 1
  print(*(dic[i] if i in dic else 0 for i in arr))
  
  ```

  * 이진탐색 문제라고 되어있지만 이진탐색으로는 못풀겠어서 사전 자료형을 활용하였더니 풀렸다

* 이분탐색 활용 풀이

  ```python
  import sys; sys.stdin = open('10816_input.txt', 'r')
  from collections import Counter
  
  
  def binary_search(target, data):
      start, end = 0, len(data)-1
      while start <= end:
          mid = (start + end) // 2
          if data[mid] == target:
              return mid
          elif data[mid] < target:
              start = mid + 1
          else:
              end = mid - 1
      return -1
  
  
  N = int(input())
  board = list(map(int, input().split()))
  M = int(input())
  arr = list(map(int, input().split()))
  c = Counter(board)
  board.sort()
  # numbers = [0] * M
  #
  # for i in range(M):
  #     if binary_search(arr[i], board) != -1:
  #         numbers[i] = c[arr[i]]
  numbers = [c[arr[i]] if binary_search(arr[i], board) != -1 else 0 for i in range(M)]
  print(*numbers)
  
  ```

  * 여기서도 for문과 if 문을 써서 numbers를 작성할 때보다 한 줄로 작성했을때가 미세하게 나마 속도가 빨랐다

