import pprint
import sys
sys.stdin = open('2589_input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
pprint.pprint(arr)
