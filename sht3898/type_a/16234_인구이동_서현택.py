import pprint
import sys
sys.stdin = open('16234_input.txt', 'r')

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    Q.append((x, y))
    visit[x][y] = 1
    tmp.append((x, y))
    SUM = arr[x][y]
    while Q:
        tmp_x, tmp_y = Q.popleft()
        for i in range(4):
            nx, ny = tmp_x + dx[i], tmp_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and L <= abs(arr[nx][ny] - arr[tmp_x][tmp_y]) <= R:
                Q.append((nx, ny))
                visit[nx][ny] = 1
                tmp.append((nx, ny))
                SUM += arr[nx][ny]
    return SUM


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
while True:
    check = 0
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                Q = deque()
                tmp = []
                total = bfs(i, j)
                if len(tmp) > 1:
                    check = 1
                    newVal = total // len(tmp)
                    while tmp:
                        ni, nj = tmp.pop()
                        arr[ni][nj] = newVal
    if check:
        result += 1
    else:
        break
print(result)