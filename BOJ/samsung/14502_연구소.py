import sys; sys.stdin = open('14502_input.txt', 'r')
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
virus = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus.append((i, j))


def move(k):
    global answer
    if k == 3:
        Q = deque()
        new_board = copy.deepcopy(board)
        # for i in range(N):
        #     for j in range(M):
        #         if new_board[i][j] == 2:
        #             Q.append((i, j))
        for i in range(len(virus)):
            Q.append(virus[i])
        while Q:
            x, y = Q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y+dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if new_board[nx][ny] == 0:
                        new_board[nx][ny] = 2
                        Q.append((nx, ny))
        cnt = 0
        for i in range(N):
            for j in range(M):
                if new_board[i][j] == 0:
                    cnt += 1
        answer = max(answer, cnt)
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                move(k+1)
                board[i][j] = 0


move(0)
print(answer)
