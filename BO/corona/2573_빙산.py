import sys
sys.stdin = open('2573_input.txt', 'r')
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
