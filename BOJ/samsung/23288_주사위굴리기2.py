import sys; sys.stdin = open('23288_input.txt', 'r')

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(N, M, K)
print(board)
