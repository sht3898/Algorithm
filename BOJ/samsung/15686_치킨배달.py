import sys; sys.stdin = open('15686_input.txt', 'r')
from itertools import combinations


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
house = []
store = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append([i, j])
        elif board[i][j] == 2:
            store.append([i, j])

pick_store = list(combinations(store, M))
result = [0] * len(pick_store)

for h in house:
    for j in range(len(pick_store)):
        MIN = int(1e9)
        for k in pick_store[j]:
            temp = abs(h[0]-k[0]) + abs(h[1]-k[1])
            MIN = min(MIN, temp)
        result[j] += MIN

print(min(result))
