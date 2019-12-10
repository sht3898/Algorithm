import pprint
import sys
sys.stdin = open('2573_input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def melt(x, y):
    visit[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
            if arr[nx][ny]:
                visit[nx][ny] = 1
                melts.append((nx, ny))
            else:
                melt(nx, ny)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0


visit = [[0] * M for _ in range(N)]
melts = []
melt(0, 0)
pprint.pprint(arr)
print(sorted(melts))
while melts:
    x, y = melts.pop()
    for i in range(4):
        n_x, n_y = x + dx[i], dy[i]
        if 0 <= n_x < N and 0 <= n_y < M:
            pass
