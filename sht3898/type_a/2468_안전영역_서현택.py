import sys; sys.stdin = open('2468_input.txt', 'r')
sys.setrecursionlimit(10000)
# 최대 크기가 100 * 100이라 깊이 제한을 기본값인 1000에서 10000으로 늘림

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def search(x, y):
    visit[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] and not visit[nx][ny]:
            search(nx, ny)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
MAX = 0
ans = 0

for i in range(N):
    for j in range(N):
        MAX = max(MAX, arr[i][j])

for k in range(1, MAX+1):
    result = 0
    maps = [[0] * N for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
                if arr[i][j] > k:
                    maps[i][j] = 1

    for i in range(N):
        for j in range(N):
            if not visit[i][j] and maps[i][j]:
                search(i, j)
                result += 1
    ans = max(result, ans)

if ans == 0:
    ans = 1
print(ans)
