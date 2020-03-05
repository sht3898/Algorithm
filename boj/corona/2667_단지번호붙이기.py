import sys
sys.stdin = open('2667_input.txt', 'r')


def solve(x, y):
    global cnt
    visit[x][y] = 1
    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and board[nx][ny]:
            cnt += 1
            solve(nx, ny)


N = int(input())
board = [list(map(int, input())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
town = []
for i in range(N):
    for j in range(N):
        if not visit[i][j] and board[i][j]:
            cnt = 1
            solve(i, j)
            town.append(cnt)
print(len(town))
for t in sorted(town):
    print(t)
