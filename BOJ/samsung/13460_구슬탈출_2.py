# import sys; sys.stdin = open('13460_input.txt', 'r')
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def move(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visit = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
rx, ry, bx, by = [0] * 4
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j
Q = deque()
Q.append((rx, ry, bx, by, 1))
visit[rx][ry][bx][by] = 1

check = 0
while Q:
    rx, ry, bx, by, depth = Q.popleft()
    if depth > 10:
        break
    for i in range(4):
        next_rx, next_ry, r_cnt = move(rx, ry, dx[i], dy[i])
        next_bx, next_by, b_cnt = move(bx, by, dx[i], dy[i])

        if board[next_bx][next_by] == 'O':
            continue
        if board[next_rx][next_ry] == 'O':
            print(depth)
            check = 1
            break
        if next_rx == next_bx and next_ry == next_by:
            if r_cnt > b_cnt:
                next_rx -= dx[i]
                next_ry -= dy[i]
            else:
                next_bx -= dx[i]
                next_by -= dy[i]
        if not visit[next_rx][next_ry][next_bx][next_by]:
            visit[next_rx][next_ry][next_bx][next_by] = 1
            Q.append((next_rx, next_ry, next_bx, next_by, depth+1))
    if check:
        break
if not check:
    print(-1)
