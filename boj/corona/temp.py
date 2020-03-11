import sys
sys.stdin = open('2636_input.txt', 'r')
from collections import deque


def search(x, y):
    empty.append((x, y))
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        empty_visit[x][y] = 1
        for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not empty_visit[nx][ny] and not board[nx][ny]:
                empty.append((nx, ny))
                empty_visit[nx][ny] = 1
                Q.append((nx, ny))


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
empty = []
cheese = deque()
empty_visit = [[0] * M for _ in range(N)]
search(0, 0)
cnt = 0
for i in range(N):
    for j in range(M):
        if (i, j) not in empty:
            cheese.append((i, j))
while cheese:
    x, y = cheese.popleft()
    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
        nx, ny = x + dx, y+ dy
        if 0 <= nx < N and 0 <= ny < M and not board[nx][ny]:
            break
    else:
        cheese.append((x, y))
