import sys; sys.stdin = open('3190_input.txt', 'r')

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
