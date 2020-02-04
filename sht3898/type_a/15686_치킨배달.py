import pprint
import sys
sys.stdin = open('15686_input.txt', 'r')


def solve(k, s):
    global ans
    if k == M:
        tsum = 0
        for h in range(len(home)):
            tmin = 1e9
            for c in combi:
                tmin = min(tmin, dist[c][h])
            tsum += tmin
        ans = min(ans, tsum)
    else:
        #
        for i in range(s, len(chicken) + (k - M) + 1):
            combi[k] = i
            solve(k+1, i+1)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 집과 치킨 가게 좌표를 저장
home, chicken = [], []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

# 모든 치킨집과 집 사이의 좌표를 저장
dist = [[0] * len(home) for _ in range(len(chicken))]
for i in range(len(chicken)):
    for j in range(len(home)):
        dist[i][j] = abs(chicken[i][0] - home[j][0]) + abs(chicken[i][1] - home[j][1])

ans = 1e9
combi = [0] * M
solve(0, 0)
print(ans)
