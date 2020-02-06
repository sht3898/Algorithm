import sys
sys.stdin = open('13460_input.txt', 'r')
import pprint
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 네방향으로 움직인다
# 첫번째에 들어갔으면 성공
# 아니라면 다시 굴림
# 파란색이 들어간다면 싫패
# 동시에 들어가도 실패
# 성공하려면 빨간색이 먼저 들어가고 파란공은 멈춰야함


def solve(rx, ry, bx, by):
    pass



N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visit = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
Q = deque()


def init():
    rx, ry, bx, by = [0] * 4
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                rx, ry = i, j
            elif arr[i][j] == 'B':
                bx, by = i, j
    Q.append((rx, ry, bx, by, 1))
    visit[rx][ry][bx][by] = 1

def move(x, y, dx, dy):
    cnt = 0
    while arr[x+dx][y+dy] != '#' and arr[x][y] != '0':
        x += dx
        y += dy
    return x, y, cnt

def bfs():
    init()
    while Q:
        rx, ry, bx, by, depth = Q.popleft()
        if depth > 10:
            break
        for i in range(4):
            n_rx, n_ry, r_cnt = move(rx, ry, dx[i], dy[i])
            n_bx, n_by, b_cnt = move(bx, by, dx[i], dy[i])
            