import sys; sys.stdin = open('14499_input.txt', 'r')

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0 for _ in range(6)]
for d in list(map(int, input().split())):
    d -= 1
    nx, ny = x+dx[d], y+dy[d]

    if 0 <= nx < N and 0 <= ny < M:
        if d == 0:
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif d == 1:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif d == 2:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        else:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

        if board[nx][ny] == 0:
            board[nx][ny] = dice[5]
        else:
            dice[5] = board[nx][ny]
            board[nx][ny] = 0
        x, y = nx, ny
        print(dice[0])
