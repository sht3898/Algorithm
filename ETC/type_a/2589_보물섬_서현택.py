import pprint
import sys
sys.stdin = open('2589_input.txt', 'r')

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    Q = deque()
    dist = [[0] * M for _ in range(N)]
    Q.append((x, y))
    dist[x][y] = 1
    while Q:
        tmp_x, tmp_y = Q.popleft()
        for i in range(4):
            nx, ny = tmp_x + dx[i], tmp_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 'L' and not dist[nx][ny]:
                Q.append((nx, ny))
                dist[nx][ny] = dist[tmp_x][tmp_y] + 1
    return max(sum(dist, [])) - 1


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            result = max(result, bfs(i, j))
print(result)
