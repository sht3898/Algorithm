import sys
sys.stdin = open('14503_input.txt', 'r')

direct = [0, 3, 2, 1]    # 0: 북, 3: 서, 2: 남, 1: 동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
start_x, start_y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]