import sys
# sys.stdin = open('n1000.txt', 'r')
sys.stdin = open('1861_input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for TC in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dist = [0] * (N**2+1)
    room = 1e9
    result = -1e9
    cnt = 1
    for x in range(N):
        for y in range(N):
            start = board[x][y]
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] - start == 1:
                    dist[start] = 1

    # for i in range(N**2, -1, -1):
    #     if dist[i] == 1:
    #         cnt += 1
    #     else:
    #         if maxV <= cnt:
    #             maxV = cnt
    #         st = i + 1
    #     cnt = 0
    for i in range(N**2, 0, -1):
        if dist[i]:
            dist[i] = dist[i+1] + 1
        else:
            dist[i] = 1
    result = max(dist)
    for i in range(1, N**2+1):
        if dist[i] == result:
            print('#{} {} {}'.format(TC, i, dist[i]))
            break
