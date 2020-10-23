import sys;
sys.stdin = open('2667_input.txt', 'r')

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
print(board)
