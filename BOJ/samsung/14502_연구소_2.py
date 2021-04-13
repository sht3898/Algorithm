import sys; sys.stdin = open('14502_input.txt', 'r')
from collections import deque
import copy


def bfs():
    global answer
    b = copy.deepcopy(board)
    for i in range(N):
        for j in range(M):
            if b[i][j] == 2:
                Q.append([i, j])
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if b[nx][ny] == 0:
                    b[nx][ny] = 2
                    Q.append([nx, ny])
    cnt = 0
    for i in b:
        cnt += i.count(0)
    answer = max(answer, cnt)


def wall(k):
    if k == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(k+1)
                board[i][j] = 0


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
answer = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
wall(0)
print(answer)
