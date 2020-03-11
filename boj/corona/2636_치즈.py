import sys
sys.stdin = open('2636_input.txt', 'r')
from collections import deque


def solve(x, y):
    visit[x][y] = 1
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                visit[nx][ny] = 1
                if board[nx][ny]:
                    melts.append((nx, ny))
                else:
                    Q.append((nx, ny))


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
time = 0
tmp = ''
while True:
    visit = [[0] * M for _ in range(N)]
    melts = []
    Q = deque()
    solve(0, 0)
    if not melts:
        break
    time += 1
    tmp = len(melts)
    while melts:
        x, y = melts.pop()
        board[x][y] = 0
print(time)
print(tmp)
