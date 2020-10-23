import pprint
import sys
sys.stdin = open('2468_input.txt', 'r')

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solve(x, y):
    Q = deque()
    visit[x][y] = 1
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and maps[nx][ny]:
                visit[nx][ny] = 1
                Q.append((nx, ny))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
MAX, MIN = -1e9, 1e9
result = -1e9
for i in range(N):
    for j in range(N):
        MAX = max(MAX, board[i][j])
        MIN = min(MIN, board[i][j])

for height in range(MIN, MAX+1):
    tmp = 0
    maps = [[0] * N for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > height:
                maps[i][j] = 1

    for i in range(N):
        for j in range(N):
            if not visit[i][j] and maps[i][j]:
                solve(i, j)
                tmp += 1
    result = max(result, tmp)

if result == 0:
    result = 1
print(result)
