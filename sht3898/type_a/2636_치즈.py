import sys; sys.stdin = open('2636_input.txt', 'r')
import pprint

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def find_cheeze(x, y):
    visit[x][y] = 1
    cheeze[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and not arr[nx][ny]:
            find_cheeze(nx, ny)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cheeze = [[1] * M for _ in range(N)]
visit = [[0] * M for _ in range(N)]
pprint.pprint(cheeze)


for i in range(N):
    check = 0
    for j in range(M):
        if not visit[i][j] and not arr[i][j]:
            find_cheeze(i, j)
            check = 1
            break
    if check:
        break

pprint.pprint(cheeze)