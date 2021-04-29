import sys; sys.stdin = open('14503_input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
print(board)
Q = deque()
Q.append([r, c])
while Q:
    x, y = Q.popleft()
    visit[x][y] = 1
    d = (d-1)%4
    nx, ny = x+dx[d], y+dy[d]
    if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and not board[nx][ny]:
        Q.append([nx, ny])
        answer += 1
