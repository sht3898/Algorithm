import pprint
import sys
sys.stdin = open('2636_input.txt', 'r')
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visit[x][y] = 1
    while Q:
        tmp_x, tmp_y = Q.popleft()
        for i in range(4):
            nx, ny = tmp_x + dx[i], tmp_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                if arr[nx][ny]:
                    visit[nx][ny] = 1
                    melts.append((nx, ny))
                else:
                    visit[nx][ny] = 1
                    Q.append((nx, ny))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while True:
    visit = [[0] * M for _ in range(N)]
    melts = []
    bfs(0, 0)
    if not len(melts):
        break
    cnt += 1
    tmp = len(melts)
    while melts:
        x, y = melts.pop()
        arr[x][y] = 0
print(cnt)
print(tmp)
