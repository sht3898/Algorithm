import sys
sys.stdin = open('4875_input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def search(x, y):
    global ans
    visit[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
            if arr[nx][ny] == 0:
                search(nx, ny)
            elif arr[nx][ny] == 3:
                ans = 1
                break


for TC in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_x, start_y = i, j
                break
    search(start_x, start_y)
    print('#{} {}'.format(TC, ans))
