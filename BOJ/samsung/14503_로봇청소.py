import sys; sys.stdin = open('14503_input.txt', 'r')
import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(r, c, d)
print(board)
