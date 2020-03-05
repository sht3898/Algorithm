import sys
sys.stdin = open('2468_input.txt', 'r')
from collections import deque


def solve(x, y, height):
    Q.append((x, y))
    visit[x][y] = 1
    while Q:
        x, y = Q.popleft()
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and board[nx][ny] > height:
                Q.append((nx, ny))
                visit[nx][ny] = 1


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
MAX, MIN = -1e9, 1e9
result = 1
for i in range(N):
    for j in range(N):
        MAX = max(board[i][j], MAX)
        MIN = min(board[i][j], MIN)

for h in range(MIN, MAX+1):
    visit = [[0] * N for _ in range(N)]
    vil = 0
    Q = deque()
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and board[i][j] > h:
                vil += 1
                solve(i, j, h)
    result = max(result, vil)
print(result)
