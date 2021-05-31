import sys; sys.stdin = open('11279_input.txt', 'r')
import heapq

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 0:
        heapq.heappush(arr, [-num, num])
    else:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
