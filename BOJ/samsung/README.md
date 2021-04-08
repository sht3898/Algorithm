# 삼성 알고리즘 풀이

## [13460_구슬탈출2](https://www.acmicpc.net/problem/13460)

* 풀이

  ```python
  from collections import deque
  

  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  
  
  def move(x, y, dx, dy):
      cnt = 0
      while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
          x += dx
          y += dy
          cnt += 1
      return x, y, cnt
  
  
  N, M = map(int, input().split())
  board = [list(input()) for _ in range(N)]
  visit = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
  rx, ry, bx, by = [0] * 4
  for i in range(N):
      for j in range(M):
          if board[i][j] == 'R':
              rx, ry = i, j
          elif board[i][j] == 'B':
              bx, by = i, j
  Q = deque()
  Q.append((rx, ry, bx, by, 1))
  visit[rx][ry][bx][by] = 1
  
  check = 0
  while Q:
      rx, ry, bx, by, depth = Q.popleft()
      if depth > 10:
          break
      for i in range(4):
          next_rx, next_ry, r_cnt = move(rx, ry, dx[i], dy[i])
          next_bx, next_by, b_cnt = move(bx, by, dx[i], dy[i])
  
          if board[next_bx][next_by] == 'O':
              continue
          if board[next_rx][next_ry] == 'O':
              print(depth)
              check = 1
              break
          if next_rx == next_bx and next_ry == next_by:
              if r_cnt > b_cnt:
                  next_rx -= dx[i]
                  next_ry -= dy[i]
              else:
                  next_bx -= dx[i]
                  next_by -= dy[i]
          if not visit[next_rx][next_ry][next_bx][next_by]:
              visit[next_rx][next_ry][next_bx][next_by] = 1
              Q.append((next_rx, next_ry, next_bx, next_by, depth+1))
      if check:
          break
  if not check:
      print(-1)
  
  ```
  
  * 처음 빨간색과 파란색이 놓인 위치에서 4방향으로 기울였을때 갈 수 있는 모든 경로를 계산
  * 4차원 배열 visit을 통해 빨간색과 파란색이 놓이는 경우를 계산하여 방문하지 않은 경우에만 계산
  * 횟수가 10번을 초과하거나 파란색이 홀이 빠지는 등의 경우를 고려하여 작성
  * 성공했다면 가장 적은 횟수로 성공한 경우를, 실패한다면 -1을 반환

## [12100_2048_easy](https://www.acmicpc.net/problem/12100)

* 풀이

  ```python
  from collections import deque
  import copy

  N = int(input())
  board = [list(map(int, input().split())) for _ in range(N)]
  answer = 0
  Q = deque()
  
  
  def get(i, j):
      if board[i][j]:
          Q.append(board[i][j])
          board[i][j] = 0
  
  
  def merge(i, j, di, dj):
      while Q:
          x = Q.popleft()
          if not board[i][j]:
              board[i][j] = x
          elif board[i][j] == x:
              board[i][j] = x*2
              i, j = i+di, j+dj
          else:
              i, j = i+di, j+dj
              board[i][j] = x
  
  
  def move(k):
      if k == 0:
          for j in range(N):
              for i in range(N):
                  get(i, j)
              merge(0, j, 1, 0)
      elif k == 1:
          for j in range(N):
              for i in range(N-1, -1, -1):
                  get(i, j)
              merge(N-1, j, -1, 0)
      elif k == 2:
          for i in range(N):
              for j in range(N):
                  get(i, j)
              merge(i, 0, 0, 1)
      else:
          for i in range(N):
              for j in range(N-1, -1, -1):
                  get(i, j)
              merge(i, N-1, 0, -1)
  
  
  def solve(cnt):
      global board, answer
      if cnt == 5:
          for i in range(N):
              answer = max(answer, max(board[i]))
          return
      b = copy.deepcopy(board)
  
      for k in range(4):
          move(k)
          solve(cnt+1)
          board = copy.deepcopy(b)
  
  
  solve(0)
  print(answer)
  
  ```
  
  * 많이 어려웠던 문제라 다시 한 번 점검이 필요



## [3190_뱀](https://www.acmicpc.net/problem/3190)

* 풀이

  ```python
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

  N = int(input())
  K = int(input())
  apple = [list(map(int, input().split())) for _ in range(K)]
  L = int(input())
  rotate = dict()
  for _ in range(L):
      k, v = input().split()
      rotate[int(k)] = v
  board = [[0]*N for _ in range(N)]
  for i, j in apple:
      board[i-1][j-1] = 1
  x, y, d, time = 0, 0, 0, 0
  snake = [[x, y]]
  while snake:
      time += 1
      nx, ny = x+dx[d], y+dy[d]
      if 0 <= nx < N and 0 <= ny < N:
          if [nx, ny] in snake:
              break
  
          if board[nx][ny] == 0:
              snake.pop(0)
              snake.append([nx, ny])
          elif board[nx][ny] == 1:
              snake.append([nx, ny])
              board[nx][ny] = 0
      else:
          break
  
      if time in rotate:
          if rotate[time] == 'L':
              d = (d-1) % 4
          elif rotate[time] == 'D':
              d = (d+1) % 4
      x, y = nx, ny
  print(time)
  ```
  
  * 뱀의 위치를 저장한 뒤 조건을 확인하면서 반복함
  * 시간을 확인하며 방향을 바꿔줌



## [13458_시험감독](https://www.acmicpc.net/problem/13458)

* 풀이

  ```python
  N = int(input())
  answer = [1] * N
  board = list(map(int, input().split()))
  sup, sub = map(int, input().split())
  for i in range(N):
      board[i] -= sup
      if board[i] < 0:
          board[i] = 0
      if board[i] % sub == 0:
          answer[i] += board[i] // sub
      else:
          answer[i] += board[i] // sub + 1
  print(sum(answer))
  ```

  * 처음에는 아래 부분이 없이 풀이 했으나 함께 기술할 반례 때문에 실패

    ```python
    if board[i] < 0:
            board[i] = 0
    ```

    ```
    1
    1
    1000000 1
    
    -999998
    ```

  * 이것을 방지하기 위해 board[i]가 0보다 작아졌을때는 board[i]를 0으로 만들어서 오류가 발생하지 않도록 함



## [14499_주사위 굴리기](https://www.acmicpc.net/problem/14499)

* 풀이

  ```python
  N, M, x, y, K = map(int, input().split())
  board = [list(map(int, input().split())) for _ in range(N)]
  
  dx = [0, 0, -1, 1]
  dy = [1, -1, 0, 0]
  dice = [0 for _ in range(6)]
  for d in list(map(int, input().split())):
      d -= 1
      nx, ny = x+dx[d], y+dy[d]
  
      if 0 <= nx < N and 0 <= ny < M:
          if d == 0:
              dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
          elif d == 1:
              dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
          elif d == 2:
              dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
          else:
              dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
  
          if board[nx][ny] == 0:
              board[nx][ny] = dice[5]
          else:
              dice[5] = board[nx][ny]
              board[nx][ny] = 0
          x, y = nx, ny
          print(dice[0])
  
  ```

  * 주사위를 굴린 방향에 맞춰 주사위의 숫자를 재설정하는 것이 중요
  * 입력 값에서는 방향이 1부터 시작하나 리스트의 인덱스는 0부터 시작하므로 입력 값에서 1씩 빼서 반복



## [14500_테트로미노](https://www.acmicpc.net/problem/14500)

* 풀이

  ```python
  N, M = map(int, input().split())
  board = [list(map(int, input().split())) for _ in range(N)]
  answer = 0
  rotate = [
      [(0,0), (0,1), (1,0), (1,1)], # ㅁ
      [(0,0), (0,1), (0,2), (0,3)], # ㅡ
      [(0,0), (1,0), (2,0), (3,0)], # ㅣ
      [(0,0), (0,1), (0,2), (1,0)],
      [(1,0), (1,1), (1,2), (0,2)],
      [(0,0), (1,0), (1,1), (1,2)], # ㄴ
      [(0,0), (0,1), (0,2), (1,2)], # ㄱ
      [(0,0), (1,0), (2,0), (2,1)],
      [(2,0), (2,1), (1,1), (0,1)],
      [(0,0), (0,1), (1,0), (2,0)],
      [(0,0), (0,1), (1,1), (2,1)],
      [(0,0), (0,1), (0,2), (1,1)], # ㅜ
      [(1,0), (1,1), (1,2), (0,1)], # ㅗ
      [(0,0), (1,0), (2,0), (1,1)], # ㅏ
      [(1,0), (0,1), (1,1), (2,1)], # ㅓ
      [(1,0), (2,0), (0,1), (1,1)],
      [(0,0), (1,0), (1,1), (2,1)],
      [(1,0), (0,1), (1,1), (0,2)],
      [(0,0), (0,1), (1,1), (1,2)]
  ]
  
  temp = 0
  for i in range(N):
      for j in range(M):
          for r in rotate:
              temp = 0
              for k in range(4):
                  try:
                      nx = i+r[k][0]
                      ny = j+r[k][1]
                      temp += board[nx][ny]
                  except IndexError:
                      continue
              answer = max(answer, temp)
  print(answer)
  ```

  * 각 모양 별로 만들 수 있는 모든 경우(19가지)를 정해서 해당하는 좌표로 갈 수 있는 x, y값을 rotate 리스트에 저장

  * 반복문을 통해 각 칸 별로 최대값을 구함

  * 평소와 같이 if 문을 통해 index 범위를 설정했을때는 시간 초과가 떳으나 try를 통해 예외처리를 했을때는 시간 초과가 되지 않았는데 정확한 이유는 더 공부를 해봐야할 것 같음

  * if 문 사용 코드(시간 초과 오류 발생)

    ```python
    temp = 0
    check = 0
    for i in range(N):
        for j in range(M):
            for r in rotate:
                temp = 0
                for k in range(4):
    
                    nx = i+r[k][0]
                    ny = j+r[k][1]
                    if 0 <= nx < N and 0 <= ny < M:
                        temp += board[nx][ny]
                        check = 1
    			if check:
                    answer = max(answer, temp)
                    check = 0
    print(answer)
    ```



## [14501_퇴사](https://www.acmicpc.net/problem/14501)

* 풀이

  ```python
  N = int(input())
  T, P = [0]*N, [0]*N
  for i in range(N):
      T[i], P[i] = map(int, input().split())
  dp = [0] * 20
  for i in range(N):
      if dp[i] > dp[i+1]:
          dp[i+1] = dp[i]
      if dp[i+T[i]] < dp[i] + P[i]:
          dp[i+T[i]] = dp[i] + P[i]
  print(dp[N])
  
  ```

  * dp 활용 문제
  * 다음 날보다 현재 날짜의 금액이 더 크다면 다음 날 dp에 현재 날짜의 dp 금액을 저장
  * 현재 날짜부터 필요한 상담 기간이 자난 후의 금액이 현재 날짜에 벌 수 있는 금액보다 적다면 상담 기간이 지난 후의 금액을 현재 날짜에 벌 수 있는 금액으로 바꿈