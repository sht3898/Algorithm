import sys; sys.stdin = open('3190_input.txt', 'r')
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def change(d, c):
    if c == 'L':
        d = (d-1) % 4
    else:
        d = (d+1) % 4
    return d


def bfs():
    direct = 1
    time = 1
    x, y = 0, 0
    snake = deque([[x, y]])
    board[x][y] = 2
    while True:
        nx, ny = x+dx[direct], y+dy[direct]
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 2:
            if not board[nx][ny] == 1:
                temp_x, temp_y = snake.popleft()
                board[temp_x][temp_y] = 0
            board[nx][ny] = 2
            snake.append([nx, ny])
            if time in rotate.keys():
                direct = change(direct, rotate[time])
            time += 1
        else:
            return time


N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
L = int(input())
rotate = {}
for _ in range(L):
    x, c = input().split()
    rotate[int(x)] = c
print(bfs())
