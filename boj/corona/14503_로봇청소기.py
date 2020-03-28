import sys
sys.stdin = open('14503_input.txt', 'r')

N, M = map(int, input().split())
setup = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
print(setup)