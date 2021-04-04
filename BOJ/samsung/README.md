# 삼성 알고리즘 풀이

## [13460_구슬탈출](https://www.acmicpc.net/problem/13460)

* [풀이](./13460_구슬탈출.py)

  ```python
  
  ```

  

## [12100_2048_easy](https://www.acmicpc.net/problem/12100)

* [풀이](./12100_2048_easy.py)

  ```python
  
  ```

  

## [3190_뱀](https://www.acmicpc.net/problem/3190)

* [풀이](./3190_뱀.py)

  ```python
  
  ```

  

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