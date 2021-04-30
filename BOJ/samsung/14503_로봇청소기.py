import sys; sys.stdin = open('14503_input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
Q = deque()
Q.append([r, c])
while Q:
    x, y = Q.popleft()
    board[x][y] = 1
    print(x, y)
    answer += 1
    check = 0
    for i in range(4):
        d = (d-i-1) % 4
        nx, ny = x+dx[d], y+dy[d]
        if not board[nx][ny]:
            Q.append([nx, ny])
            check = 1
            break
    if check:
        continue

    if d == 0:
        if not board[x+1][y]:
            Q.append([x+1, y])
        else:
            break
    elif d == 1:
        if not board[x][y-1]:
            Q.append([x, y-1])
        else:
            break
    elif d == 2:
        if not board[x-1][y]:
            Q.append([x-1, y])
        else:
            break
    elif d == 3:
        if not board[x][y+1]:
            Q.append([x, y+1])
        else:
            break
print(answer)
