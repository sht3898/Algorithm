# import sys; sys.stdin = open('13458_input.txt', 'r')

N = int(input())
answer = [1] * N
board = list(map(int, input().split()))
sup, sub = map(int, input().split())
for i in range(N):
    board[i] -= sup
    if board[i] < 0:
        board[i] = 0
    if board[i] % sub == 0:
        answer[i] += board[i] // sub
    else:
        answer[i] += board[i] // sub + 1
print(sum(answer))
