import sys; sys.stdin = open('4616_input.txt')
import pprint


dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]


# def othello(x, y, color, d_x, d_y):
#     maps[x][y] = color
#     if d_x == 0 and d_y == 0:
#         for k in range(8):
#             nx, ny = x + dx[k], y + dy[k]
#             if 0 < nx <= N and 0 < ny <= N:
#                 if maps[nx][ny] == 1 and color == 2:
#                     othello(nx, ny, 2, dx[k], dy[k])
#                 elif maps[nx][ny] == 2 and color == 1:
#                     othello(nx, ny, 1, dx[k], dy[k])
#     else:
#         nx, ny = x + d_x, y + d_y
#         if 0 < nx <= N and 0 < ny <= N:
#             if maps[nx][ny] == 1 and color == 2:
#                 othello(nx, ny, 2, d_x, d_y)
#             elif maps[nx][ny] == 2 and color == 1:
#                 othello(nx, ny, 1, d_x, d_y)


for TC in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    maps = [[0] * (N+1) for _ in range(N+1)]
    maps[N//2][N//2] = 2
    maps[N//2+1][N//2+1] = 2
    maps[N//2+1][N//2] = 1
    maps[N//2][N//2+1] = 1
    black, white = 0, 0

    for stone in arr:
        y, x, color = stone[0], stone[1], stone[2]
        # othello(x, y, color, 0, 0)

    for i in range(N+1):
        for j in range(N+1):
            if maps[i][j] == 1:
                black += 1
            elif maps[i][j] == 2:
                white += 1
    pprint.pprint(maps)
    print('#{} {} {}'.format(TC, black, white))
