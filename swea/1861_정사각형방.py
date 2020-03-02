import sys
sys.stdin = open('1861_input.txt', 'r')
sys.setrecursionlimit(10000)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solve(x, y):
    global cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] - board[x][y] == 1:
            cnt += 1
            solve(nx, ny)
            break


for TC in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    room = 1e9
    result = -1e9
    for i in range(N):
        for j in range(N):
            start = board[i][j]
            cnt = 1
            solve(i, j)
            if cnt > result:
                room, result = start, cnt
            elif cnt == result and start < room:
                room, result = start, cnt
    print('#{} {} {}'.format(TC, room, result))
