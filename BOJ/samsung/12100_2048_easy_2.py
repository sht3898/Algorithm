import sys; sys.stdin = open('12100.txt', 'r')
from collections import deque
import copy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
Q = deque()


def get(i, j):
    if board[i][j]:
        Q.append(board[i][j])
        board[i][j] = 0


def merge(i, j, di, dj):
    while Q:
        x = Q.popleft()
        if not board[i][j]:
            board[i][j] = x
        elif board[i][j] == x:
            board[i][j] = x*2
            i, j = i+di, j+dj
        else:
            i, j = i+di, j+dj
            board[i][j] = x


def move(k):
    if k == 0:
        for j in range(N):
            for i in range(N):
                get(i, j)
            merge(0, j, 1, 0)
    elif k == 1:
        for j in range(N):
            for i in range(N-1, -1, -1):
                get(i, j)
            merge(N-1, j, -1, 0)
    elif k == 2:
        for i in range(N):
            for j in range(N):
                get(i, j)
            merge(i, 0, 0, 1)
    else:
        for i in range(N):
            for j in range(N-1, -1, -1):
                get(i, j)
            merge(i, N-1, 0, -1)


def solve(cnt):
    global board, answer
    if cnt == 5:
        for i in range(N):
            answer = max(answer, max(board[i]))
        return
    b = copy.deepcopy(board)

    for k in range(4):
        move(k)
        solve(cnt+1)
        board = copy.deepcopy(b)


solve(0)
print(answer)
