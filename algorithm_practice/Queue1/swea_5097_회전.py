import sys; sys.stdin = open('5097_input.txt', 'r')
from collections import deque

for TC in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    Q = deque()
    for i in arr:
        Q.append(i)
    for _ in range(M):
        Q.append(Q.popleft())
    print('#{} {}'.format(TC, Q.popleft()))
