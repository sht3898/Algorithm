import sys; sys.stdin = open('1210_input.txt', 'r')

dx = [-1, 0, 0]
dy = [0, 1, -1]


def dfs(x, y):
    global result
    visit[x][y] = 1
    stack.append([x, y])
    while stack:
        temp = stack.pop()
        if temp[0] == 0:
            result = temp[1]
            break
        for i in range(3):
            nx, ny = temp[0] + dx[i], temp[1] + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100 and not visit[nx][ny] and arr[nx][ny] == 1:
                visit[nx][ny] = 1
                stack.append([nx, ny])


for _ in range(1, 11):
    TC = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    visit = [[0] * 100 for _ in range(100)]
    stack = []
    result = 0
    for i in range(100):
        if arr[99][i] == 2:
            start_y = i
            break
    dfs(99, start_y)
    print('#{} {}'.format(TC, result))
