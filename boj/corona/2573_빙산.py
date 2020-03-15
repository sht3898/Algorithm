import sys
sys.stdin = open('2573_input.txt', 'r')

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
year = 0
print(board)
