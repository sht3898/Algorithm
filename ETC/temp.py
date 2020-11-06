import sys
sys.stdin = open('temp.txt', 'r')
from _collections import deque


def bfs(x, y, cnt):
    visit[x][y] = 1
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        # 4방향 돌면서 안간 곳 점검
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = x + dx, y + dy
            # 방문안한 곳이 있다면 cnt에 1을 더해서 현재 탐색 중인 칸의 개수를 늘림
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and board[nx][ny]:
                visit[nx][ny] = 1
                Q.append((nx, ny))
                cnt += 1
    return cnt


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
result = []
Q = deque()
for i in range(n):
    for j in range(m):
        if not visit[i][j] and board[i][j]:
            # 자기 칸도 세야되니까 0이 아닌 1부터 시작
            result.append(bfs(i, j, 1))

print(len(result), max(result))
