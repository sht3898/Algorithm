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

