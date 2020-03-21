import sys
sys.stdin = open('2589_input.txt', 'r')


def dfs(x, y, k):
    global MAX
    visit[x][y] = 1
    MAX = max(MAX, k)
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and board[nx][ny] == 'L':
            dfs(nx, ny, k+1)


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
MAX = -1e9
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            visit = [[0] * M for _ in range(N)]
            dfs(i, j, 0)
print(MAX)
