import pprint
import sys
sys.stdin = open('2636_input.txt', 'r')
sys.setrecursionlimit(10000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    visit[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
            if arr[nx][ny]:
                visit[nx][ny] = 1
                melt.append((nx, ny))
            else:
                dfs(nx, ny)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while True:
    visit = [[0] * M for _ in range(N)]
    melt = []
    dfs(0, 0)
    pprint.pprint(arr)
    print(sorted(melt))
    print()
    if not len(melt):
        break
    cnt += 1
    tmp = len(melt)
    while melt:
        x, y = melt.pop()
        arr[x][y] = 0
print(cnt)
print(tmp)
