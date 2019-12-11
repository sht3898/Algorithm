import pprint
import sys
sys.stdin = open('2573_input.txt', 'r')
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def search(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
            lake[x][y] += 1


def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visit[x][y] = 1
    while Q:
        tmp_x, tmp_y = Q.popleft()
        for i in range(4):
            nx, ny = tmp_x + dx[i], tmp_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and arr[nx][ny]:
                visit[nx][ny] = 1
                Q.append((nx, ny))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
year = 0
while True:
    year += 1
    lake = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            search(i, j)

    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                arr[i][j] = max(0, arr[i][j] - lake[i][j])
    cnt = 0
    visit = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and arr[i][j]:
                cnt += 1
                bfs(i, j)
    if cnt >= 2:
        print(year)
        break
    elif cnt == 0:
        print(0)
        break
