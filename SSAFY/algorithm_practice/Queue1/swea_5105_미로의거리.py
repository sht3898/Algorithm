import sys; sys.stdin = open('5105_input.txt', 'r')
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    global result
    Q.append((x, y))
    visit[x][y] = 1
    while Q:
        start_x, start_y = Q.popleft()
        for i in range(4):
            nx, ny = start_x + dx[i], start_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and (arr[nx][ny] == 0 or arr[nx][ny] == 3):
                Q.append((nx, ny))
                visit[nx][ny] = 1
                dist[nx][ny] = dist[start_x][start_y] + 1
                if arr[nx][ny] == 3:
                    result = dist[nx][ny] - 1
                    return


for TC in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    Q = deque()
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                sx, sy = i, j
                break
    bfs(sx, sy)
    print('#{} {}'.format(TC, result))
