import sys;
sys.stdin = open('3190_input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
rotation = dict()
L = int(input())
for _ in range(L):
    s, r = input().split()
    rotation[int(s)] = r
d = 0
t = 0
snake = [[0, 0]]
while snake:
    t += 1
    x, y = snake[-1][0], snake[-1][1]
    nx, ny = x+dx[d], y+dy[d]
    if 0 <= nx < N and 0 <= ny < N:
        # 자기 자신과 부딪혔을때
        if [nx, ny] in snake:
            break

        if board[nx][ny] == 1:
            snake.append([nx, ny])
            board[nx][ny] = 0

        elif board[nx][ny] == 0:
            snake.pop(0)
            snake.append([nx, ny])

    # 벽과 부딪혔을때
    else:
        break


    if t in rotation:
        if rotation[t] == 'L':
            d = (d-1) % 4
        elif rotation[t] == 'D':
            d = (d+1) % 4

print(t)
