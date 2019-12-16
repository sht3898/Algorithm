import pprint
import sys
sys.stdin = open('14502_input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    arr[x][y] = 2
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
            dfs(nx, ny)


def solve(k, s):
    global result
    if k == 3:
        for i in range(3):
            x, y = safe_zone[combi[i]]
            arr[x][y] = 1
        for x, y in virus_zone:
            dfs(x, y)
        result = max(result, sum(arr, []).count(0))

        for i in range(N):          # 원상복구
            for j in range(M):
                arr[i][j] = backup[i][j]
    else:
        for i in range(s, len(safe_zone) + k - 2):
            combi[k] = i
            solve(k+1, i+1)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
safe_zone = []      # 안전한 위치 저장
virus_zone = []     # 바이러스 위치 저장
backup = [[0] * M for _ in range(N)]    # arr 보관하기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            safe_zone.append((i, j))
        elif arr[i][j] == 2:
            virus_zone.append((i, j))
        backup[i][j] = arr[i][j]    # arr 값 옮기기
result = 0      # 결과를 저장
combi = [0] * 3 #
solve(0, 0)
print(result)
