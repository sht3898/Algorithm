import sys
sys.stdin = open('1100_input.txt', 'r')

arr = [list(input()) for _ in range(8)]
board = [[''] * 8 for _ in range(8)]
white = []
before = 0  # 0: white
result = 0
for i in range(8):
    for j in range(8):
        if i % 2:
            if before:
                board[i][j] = 1
                before = 0
            else:
                board[i][j] = 0
                before = 1
        else:
            if before:
                board[i][j] = 0
                before = 0
            else:
                board[i][j] = 1
                before = 1

for i in range(8):
    for j in range(8):
        if board[i][j]:
            white.append((i, j))

for i in range(8):
    for j in range(8):
        if arr[i][j] == 'F' and (i, j) in white:
            result += 1

print(result)
