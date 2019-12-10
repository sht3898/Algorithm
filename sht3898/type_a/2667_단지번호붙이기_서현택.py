import sys; sys.stdin = open('2667_input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def search(x, y):
    global tmp
    visit[x][y] = 1
    tmp += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and arr[nx][ny]:
            search(nx, ny)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
result = 0
cnt = []

for i in range(N):
    for j in range(N):
        if arr[i][j] and not visit[i][j]:
            tmp = 0
            search(i, j)
            result += 1
            cnt.append(tmp)

print(result)
for i in sorted(cnt):
    print(i)
