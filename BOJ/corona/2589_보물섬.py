import sys
sys.stdin = open('2589_input.txt', 'r')
from collections import deque


def bfs(x, y, k):
    global MAX
    visit[x][y] = 1
    Q.append((x, y, k))
    while Q:
        x, y, k = Q.popleft()
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and board[nx][ny] == 'L':
                visit[nx][ny] = 1
                Q.append((nx, ny, k+1))
                MAX = max(MAX, k+1)


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
Q = deque()
MAX = -1e9
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            visit = [[0] * M for _ in range(N)]
            bfs(i, j, 0)
print(MAX)
