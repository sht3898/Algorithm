import sys; sys.stdin = open('15686_input.txt', 'r')


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = int(1e9)
check = [0] * M
house = []
store = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append([i, j])
        elif board[i][j] == 2:
            store.append([i, j])

dist = [[0]*len(store) for _ in range(len(house))]
for i in range(len(house)):
    for j in range(len(store)):
        dist[i][j] = abs(house[i][0]-store[j][0]) + abs(house[i][1] - store[j][1])
print(dist)
