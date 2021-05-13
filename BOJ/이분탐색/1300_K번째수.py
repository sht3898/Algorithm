import sys; sys.stdin = open('1300_input.txt', 'r')

N = int(input())
k = int(input())
start, end = 1, k
while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N)

    if temp < k:
        start = mid + 1
    else:
        end = mid - 1
print(start)
