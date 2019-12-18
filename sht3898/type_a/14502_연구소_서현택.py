import pprint
import sys
sys.stdin = open('14502_input.txt', 'r')
from copy import deepcopy
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    Q = deque()
    arr[x][y] = 2
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
                arr[nx][ny] = 2
                Q.append((nx, ny))


def solve(k, s):
    global result
    if k == 3:
        for i in range(3):
            x, y = safe_zone[comb[i]]
            arr[x][y] = 1
        for x, y in virus_zone:
            bfs(x, y)
        result = max(result, sum(arr, []).count(0))

        for i in range(N):
            for j in range(M):
                arr[i][j] = backup[i][j]
    else:
        for i in range(s, len(safe_zone) - 1 + (k - 1)):
            comb[k] = i
            solve(k+1, i+1)


N, M = map(int, input().split())    # 세로, 가로
arr = [list(map(int, input().split())) for _ in range(N)]   # 지도, 0: 빈칸, 1:벽, 2: 바이러스
safe_zone = []
virus_zone = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            safe_zone.append((i, j))
        elif arr[i][j] == 2:
            virus_zone.append((i, j))
backup = deepcopy(arr)
result = 0
comb = [0] * 3  # 벽의 좌표 저장할 곳
solve(0, 0)
print(result)
