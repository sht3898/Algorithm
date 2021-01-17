import sys;sys.stdin = open('3190_input.txt', 'r')
import pprint

N = int(input())
K = int(input())
board = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    a, b = map(int, input().split())
    board[a][b] = 1
pprint.pprint(board)
direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]

L = int(input())
arr = [list(input().split()) for _ in range(L)]
now = (1, 1)
print(arr)
