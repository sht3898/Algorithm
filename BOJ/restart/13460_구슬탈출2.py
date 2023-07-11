import sys;
sys.stdin = open("13460_input.txt", "r")

N, M = map(int, input().split())
blue = []
red = []
hole = []
board = []
# board = [list(input()) for _ in range(M)]
for j in range(M):
    temp = list(input())
    board.append(temp)
    for i in range(len(temp)):
        if temp[i] == 'B':
            blue.append([j, i])
        elif temp[i] == 'R':
            red.append([j, i])
        elif temp[i] == 'O':
            hole.append([j, i])
answer = 0
print(board)
print(red, blue, hole)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
