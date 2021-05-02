import sys; sys.stdin = open('14503_input.txt', 'r')


def robot(x, y, d):
    if visit[x][y] and board[x][y] == 0:

        return


N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(board)
