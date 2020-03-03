# SWEA

## [1952_수영장](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq)

* 풀이

  ```python
  def solve(k, s):
      global MIN
      if k >= 13:
          MIN = min(MIN, s)
      else:
          solve(k+1, s+fees[0]*plans[k])
          solve(k+1, s+fees[1])
          solve(k+3, s+fees[2])
  
  
  for TC in range(1, int(input())+1):
      fees = list(map(int, input().split()))
      plans = [0] + list(map(int, input().split()))
      MIN = fees[3]
      solve(1, 0)
      print('#{} {}'.format(TC, MIN))
  
  ```

  

## [4008_숫자만들기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH)

* 풀이

  ```python
  def solve(k, plus, minus, multiple, divide, s):
      global MAX, MIN
      if k == N:
          MAX = max(MAX, s)
          MIN = min(MIN, s)
      else:
          if plus:
              solve(k+1, plus-1, minus, multiple, divide, s+numbers[k])
          if minus:
              solve(k+1, plus, minus-1, multiple, divide, s-numbers[k])
          if multiple:
              solve(k+1, plus, minus, multiple-1, divide, s*numbers[k])
          if divide:
              if s >= 0:
                  solve(k+1, plus, minus, multiple, divide-1, s // numbers[k])
              elif s < 0:
                  solve(k+1, plus, minus, multiple, divide-1, -(-s // numbers[k]))
  
  
  for TC in range(1, int(input())+1):
      N = int(input())
      arr = list(map(int, input().split()))   # +, -, *, / 개수
      numbers = list(map(int, input().split()))   # 주어진 숫자
      MAX = -1e9
      MIN = 1e9
      solve(1, arr[0], arr[1], arr[2], arr[3], numbers[0])
      print('#{} {}'.format(TC, MAX - MIN))
  
  ```

* solve 할 때, solve(0, arr[0], arr[1], arr[2], arr[3], 0)로 하면 안 되는 이유가 궁금



## [1861_정사각형방](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LtJYKDzsDFAXc)

* 풀이

  ```python
  sys.setrecursionlimit(10000)
  
  
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  
  
  def solve(x, y):
      global cnt
      for i in range(4):
          nx, ny = x + dx[i], y + dy[i]
          if 0 <= nx < N and 0 <= ny < N and board[nx][ny] - board[x][y] == 1:
              cnt += 1
              solve(nx, ny)
              break
  
  
  for TC in range(1, int(input())+1):
      N = int(input())
      board = [list(map(int, input().split())) for _ in range(N)]
      room = 1e9
      result = -1e9
      for i in range(N):
          for j in range(N):
              start = board[i][j]
              cnt = 1
              solve(i, j)
              if cnt > result:
                  room, result = start, cnt
              elif cnt == result and start < room:
                  room, result = start, cnt
      print('#{} {} {}'.format(TC, room, result))
  
  ```

  * pypy로 하지 않으면 재귀 오류가 뜨기 때문에 sys.setrecursionlimit(10000)를 통해 재귀의 제한을 늘림

* 다른 방식의 풀이

  ```python
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  
  
  for TC in range(1, int(input())+1):
      N = int(input())
      board = [list(map(int, input().split())) for _ in range(N)]
      dist = [0] * (N**2+1)
      room = 1e9
      result = -1e9
      cnt = 1
      for x in range(N):
          for y in range(N):
              start = board[x][y]
              for k in range(4):
                  nx, ny = x + dx[k], y + dy[k]
                  if 0 <= nx < N and 0 <= ny < N and board[nx][ny] - start == 1:
                      dist[start] = 1
  
      for i in range(N**2, 0, -1):
          if dist[i]:
              dist[i] = dist[i+1] + 1
          else:
              dist[i] = 1
      result = max(dist)
      for i in range(1, N**2+1):
          if dist[i] == result:
              print('#{} {} {}'.format(TC, i, dist[i]))
              break
  
  ```

  * 최대로 갈 수 있는 거리를 저장할 변수 dist를 N*N 이차원 배열이 아니라 N\*N 크기의 일차원 배열로 만들어 시간복잡도를 줄임

  

## [1865_동철이의일분배](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc)

* 풀이

  ```python
  def solve(k):
      global sub_result, result
  
      if sub_result <= result:
          return
  
      if k == N:
          result = sub_result
          return
  
      for j in range(N):
          if not visit[j]:
              if arr[k][j] == 0:
                  continue
              else:
                  sub_result *= (arr[k][j]/100)
                  visit[j] = 1
                  solve(k+1)
                  sub_result /= (arr[k][j]/100)
                  visit[j] = 0
  
  
  for TC in range(1, int(input())+1):
      N = int(input())
      arr = [list(map(int, input().split())) for _ in range(N)]
      visit = [0] * N
      sub_result, result = 1, 0
      solve(0)
      print('#{0} {1:.6f}'.format(TC, round(result*100, 6)))
  
  ```

  * 출력 fotmat: {number: round}
  * number에서는 format 함수 안의 값 중 몇 번째 값을 순서대로 넣을 것인지 결정
  * round에서는 .6f 와 같은 형태로 변수를 소수점 6자리까지 float 형태로 표현하겠다는 의미를 나타냄