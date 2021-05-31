import sys; sys.stdin = open('1927_input.txt', 'r')
import heapq

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 0:
        heapq.heappush(arr, num)
    else:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
