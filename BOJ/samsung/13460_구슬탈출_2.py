import sys; sys.stdin = open('13460_input.txt', 'r')
from collections import deque


def move(r, b, x, y):
    nrx, nry = r[0]+x, r[1]+y
    nbx, nby = b[0]+x, b[1]+y


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
red, blue = [0, 0], [0, 0]
hole = [0, 0]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red = [i, j]
        elif board[i][j] == 'B':
            blue = [i, j]
        elif board[i][j] == 'O':
            hole = [i, j]

cnt = 0
while True:
    cnt += 1
    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
        pass