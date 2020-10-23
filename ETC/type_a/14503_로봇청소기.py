import pprint
import sys
sys.stdin = open('14503_input.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
direction = [3, 0, 1, 2]
print(d)
pprint.pprint(board)
pprint.pprint(visit)