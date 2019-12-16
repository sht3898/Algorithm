import pprint
import sys
sys.stdin = open('14502_input.txt', 'r')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
safe_zone = []
virus_zone = []
backup = [[0] * M for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            safe_zone.append((i, j))
        elif arr[i][j] == 2:
            virus_zone.append((i, j))
        backup[i][j] = arr[i][j]
