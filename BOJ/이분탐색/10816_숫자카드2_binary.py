import sys; sys.stdin = open('10816_input.txt', 'r')
from collections import Counter


def binary_search(target, data):
    start, end = 0, len(data)-1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


N = int(input())
board = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
c = Counter(board)
board.sort()
# numbers = [0] * M
#
# for i in range(M):
#     if binary_search(arr[i], board) != -1:
#         numbers[i] = c[arr[i]]
numbers = [c[arr[i]] if binary_search(arr[i], board) != -1 else 0 for i in range(M)]
print(*numbers)
