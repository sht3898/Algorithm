import sys;
sys.stdin = open("13460_input.txt", "r")

N, M = map(int, input().split())
board = [list(input()) for _ in range(M)]
answer = 0
print(board)