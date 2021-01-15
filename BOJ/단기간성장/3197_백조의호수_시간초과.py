import sys;sys.stdin = open('3197_input.txt', 'r')
from collections import deque


def dfs(x, y):
    global check
    Q.append((x, y))
    visit[x][y] = 1
    while Q:
        x, y = Q.popleft()
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C and not visit[nx][ny] and board[nx][ny] != 'X':
                if board[nx][ny] == '.':
                    Q.append((nx, ny))
                    visit[nx][ny] = 1
                elif board[nx][ny] == 'L':
                    check = 1
                    break


def melt():
    melt_spot = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                melt_spot.append((i, j))
    for x, y in melt_spot:
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == 'X':
                board[nx][ny] = '.'


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]   # .: 물, X: 빙판, L: 백조
Q = deque()
check = 0
day = 0
while True:
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'L':
                visit = [[0]*C for _ in range(R)]
                dfs(i, j)
                break
    if check:
        print(day)
        break
    melt()
    day += 1
