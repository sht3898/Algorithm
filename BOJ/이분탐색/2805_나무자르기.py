import sys
sys.stdin = open('2805_input.txt', 'r')

N, M = map(int, input().split())
board = list(map(int, input().split()))
start = 1
end = max(board)
while start <= end:
    mid = (start + end)//2
    total = sum(b-mid for b in board if b > mid)
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
