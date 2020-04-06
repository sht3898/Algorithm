import sys
sys.stdin = open('14503_input.txt', 'r')
from collections import deque

# 서, 남, 동, 북
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
direction = [0, 3, 2, 1]
back = [2, 1, 0, 3]


def solve(x, y, d):
    Q = deque()
    visit[x][y] = 1
    cnt = 1
    Q.append((x, y, d))
    while Q:
        x, y, d = Q.popleft()
        flag = 0
        for i in range(4):
            nd = direction[d]
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and not board[nx][ny]:
                visit[nx][ny] = 1
                cnt += 1
                Q.append((nx, ny, nd))
                flag = 1
                break

        if not flag:
            nd = back[d]
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < N and 0 <= ny < M and not board[nx][ny]:
                Q.append((nx, ny, d))
    return cnt


N, M = map(int, input().split())
start_x, start_y, start_d = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
result = solve(start_x, start_y, start_d)
print(result)
