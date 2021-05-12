import sys; sys.stdin = open('2110_input.txt', 'r')


N, C = map(int, input().split())
board = list(int(input()) for _ in range(N))
board.sort()
start, end = 1, board[-1]-board[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    old = board[0]
    count = 1

    for i in range(1, N):
        if board[i] - old >= mid:
            count += 1
            old = board[i]
    if count >= C:
        start = mid + 1
    else:
        end = mid-1
print(end)
