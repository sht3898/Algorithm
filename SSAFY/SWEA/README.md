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



## [3752_가능한시험점수](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWHPkqBqAEsDFAUn)

* 풀이

  ```python
  def solve(k, s):
      if k == N:
          result.add(s)
          return
      if visit[k][s]:
          return
      else:
          visit[k][s] = 1
          solve(k+1, s+arr[k])
          solve(k+1, s)
  
  
  for TC in range(1, int(input())+1):
      N = int(input())
      arr = list(map(int, input().split()))
      visit = [[0] * 10000 for _ in range(N)]
      result = set()
      solve(0, 0)
      print('#{0} {1}'.format(TC, len(result)))
  ```

  * 처음에는 visit 을 통해 arr 요소들의 방문 여부를 따져서 풀었는데 시간 초과 오류 뜸
  * visit에 각 단계에서 10000까지의 숫자 중 해당하는 것을 통과했나 저장해서 풀었더니 통과
  * 그래도 시간이 오래걸림

* 무연이형 풀이

  ```python
  for TC in range(1, int(input())+1):
      N = int(input())
      arr = list(map(int, input().split()))
      result = set({0})
      for i in range(N):
          tmp = set()
          for n in result:
              tmp.add(n+arr[i])
          result = result | tmp
      print('#{0} {1}'.format(TC, len(result)))
  ```

  * set에 미리 0을 저장해둔 뒤에 간단한 반복문을 통해 값을 저장함
  * result = result | tmp은 합집합을 찾기 위한 구문
  * result와 tmp를 중복 제외하고 합치는 문법

* 진희 누나 풀이

  ```python
  for TC in range(1, int(input())+1):
      N = int(input())
      arr = list(map(int, input().split()))
      result = set({0})
      for i in arr:
          tmp = set()
          for n in result:
              tmp.add(n+i)
          result = result.union(tmp)
      print('#{} {}'.format(TC, len(result)))
  
  ```

  * 무연이형 풀이와 거의 유사하지만 합집합(|) 문법 대신 union을 통해 두 집합자료형을 합침

* [집합자료형 참고링크](https://wikidocs.net/1015#_3)



