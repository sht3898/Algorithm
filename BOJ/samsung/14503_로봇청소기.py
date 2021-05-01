import sys; sys.stdin = open('14503_input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 1
visit[r][c] = 1
Q = deque()
Q.append([r, c, d])
while Q:
    x, y, d = Q.popleft()
    check = 0
    for i in range(4):
        d = (d-1) % 4
        nx, ny = x+dx[d], y+dy[d]
        if not board[nx][ny] and not visit[nx][ny]:
            visit[nx][ny] = 1
            answer += 1
            check = 1
            Q.append([nx, ny, d])
            break
    if check:
        continue

    nx, ny = x-dx[d], y-dy[d]
    if board[nx][ny] == 0:
        Q.append([nx, ny, d])
print(answer)
