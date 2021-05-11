import sys
sys.stdin = open('1654_input.txt', 'r')

K, N = map(int, input().split())
board = [int(input()) for _ in range(K)]
start, end = 1, max(board)
while start <= end:
    mid = (start + end) // 2
    total = sum(b//mid for b in board)
    if total >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
