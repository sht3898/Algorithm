import sys; sys.stdin = open('3197_input.txt', 'r')
from collections import deque

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
print(board)