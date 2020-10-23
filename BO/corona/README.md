# Baejoon

## [2636_치즈](https://www.acmicpc.net/problem/2636)

* 풀이

  ```python
  from collections import deque
  
  
  def solve(x, y):
      visit[x][y] = 1
      Q.append((x, y))
      while Q:
          x, y = Q.popleft()
          for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
              nx, ny = x + dx, y + dy
              if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                  visit[nx][ny] = 1
                  if board[nx][ny]:
                      melts.append((nx, ny))
                  else:
                      Q.append((nx, ny))
  
  
  N, M = map(int, input().split())
  board = [list(map(int, input().split())) for _ in range(N)]
  time = 0
  tmp = ''
  while True:
      visit = [[0] * M for _ in range(N)]
      melts = []
      Q = deque()
      solve(0, 0)
      if not melts:
          break
      time += 1
      tmp = len(melts)
      while melts:
          x, y = melts.pop()
          board[x][y] = 0
  print(time)
  print(tmp)
  
  ```

  * dfs로 풀면 런타임 오류 발생 => bfs로 풀이
  * 가장 바깥 쪽 줄은 공백이므로 여기로 bfs로 실시하여 빈칸이면 체크하고, 1이면 녹을 목록에 추가
  * 녹을 목록을 순환하며 한 차례가 지날때마다 board에서 해당 부분을 0으로 바꿈
  
  

# [2573_빙산](https://www.acmicpc.net/problem/2573)

* 풀이

  ```python
  from collections import deque
  
  
  def search(x, y):
      for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
          nx, ny = x + dx, y + dy
          if 0 <= nx < N and 0 <= ny < M and not board[nx][ny]:
              arr[x][y] += 1
  
  
  def island(x, y):
      Q = deque()
      Q.append((x, y))
      visit[x][y] = 1
      while Q:
          x, y = Q.popleft()
          for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
              nx, ny = x + dx, y + dy
              if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and board[nx][ny]:
                  visit[nx][ny] = 1
                  Q.append((nx, ny))
  
  
  N, M = map(int, input().split())
  board = [list(map(int, input().split())) for _ in range(N)]
  year = 1
  result = 0
  while True:
      cnt = 0
      arr = [[0] * M for _ in range(N)]
      visit = [[0] * M for _ in range(N)]
  
      for i in range(N):
          for j in range(M):
              if board[i][j]:
                  search(i, j)
  
      for i in range(N):
          for j in range(M):
              if board[i][j]:
                  board[i][j] = max(0, board[i][j] - arr[i][j])
  
      for i in range(N):
          for j in range(M):
              if not visit[i][j] and board[i][j]:
                  cnt += 1
                  island(i, j)
  
      if cnt >= 2:
          result = year
          break
      elif cnt == 0:
          result = 0
          break
  
      year += 1
  
  print(result)
  
  ```

  * 주어진 배열과 같은 크기의 새로운 배열을 만들고 dfs로 순회하면서 얼음이 있는 칸에서 주변에 0이 몇칸있나 확인하여 저장
  * 저장이 끝났을때 다시 모든 배열을 순회하며 board에 녹은 얼음을 빼준다. 이때 얼음이 0보다 작으면 0으로 만들어준다.
  * 다시 모든 배열을 순회하며 섬의 갯수를 셈
  * 섬이 2개 이상으로 나뉘어 졌다면 반복을 멈추고 결과를 출력
  * 섬이 나누어 지지 않았다면 result (0)을 출력
  * 섬의 갯수를 찾을때 dfs로 하면 런타임 오류가 발생하기 때문에, bfs로 찾음

## [2589_보물섬](https://www.acmicpc.net/problem/2589)

* 풀이

  ```python
  from collections import deque
  
  
  def bfs(x, y, k):
      global MAX
      visit[x][y] = 1
      Q.append((x, y, k))
      while Q:
          x, y, k = Q.popleft()
          for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
              nx, ny = x + dx, y + dy
              if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and board[nx][ny] == 'L':
                  visit[nx][ny] = 1
                  Q.append((nx, ny, k+1))
                  MAX = max(MAX, k+1)
  
  
  N, M = map(int, input().split())
  board = [list(input()) for _ in range(N)]
  Q = deque()
  MAX = -1e9
  for i in range(N):
      for j in range(M):
          if board[i][j] == 'L':
              visit = [[0] * M for _ in range(N)]
              bfs(i, j, 0)
  print(MAX)
  
  ```

* 각 칸에서 출발할 때 가장 오랜 시간이 걸리는 구간을 계산

* 함수 bfs의 if 문 안에서 k += 1로 k 값을 미리 계산하면 아직 4방향 중 가지못한 방향의 k 값의 영향을 미치기 때문에 Q와 MAX를 계산할 때 반영

* bfs로 풀이

