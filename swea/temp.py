import sys
sys.stdin = open('1861_input.txt', 'r')
sys.setrecursionlimit(10000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    dist[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] - board[x][y] == 1:
            if dist[nx][ny] == 0:
                dfs(nx, ny)
            dist[x][y] = max(dist[x][y], dist[nx][ny] + 1)


for TC in range(1, int(input())+1):
    N = int(input())
    result = -1e9
    room = 1e9
    board = [list(map(int, input().split())) for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if dist[i][j] == 0:
                dfs(i, j)

    for i in range(N):
        for j in range(N):
            if result <= dist[i][j]:
                result = dist[i][j]
                room = min(room, board[i][j])
    print('#{} {} {}'.format(TC, room, result))
