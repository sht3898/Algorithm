import sys
sys.stdin = open('1920_input.txt', 'r')

N = int(input())
board = list(map(int, input().split()))
board.sort()
M = int(input())
for num in list(map(int, input().split())):
    start, end = 0, len(board) - 1
    check = 0
    while start <= end:
        mid = (start + end) // 2
        if num == board[mid]:
            check = 1
            break
        elif board[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    print(check)
