import sys; sys.stdin = open('5099_input.txt', 'r')
from collections import deque

for TC in range(1, int(input())+1):
    N, M = map(int, input().split())    # N: 화덕의 용량, M: 피자 개수
    arr = list(map(int, input().split()))   # 치즈의 양
    pizzas = [[arr[i], i+1] for i in range(M)]
    Q = deque()
    for _ in range(N):
        Q.append(pizzas.pop(0))

    while Q:
        if len(Q) == N:
            if Q[0][0] == 0:
                Q.popleft()
            else:
                Q.append(Q.popleft())
                Q[-1][0] = Q[-1][0] // 2
        else:
            if pizzas:
                Q.appendleft(pizzas.pop(0))
            else:
                if Q[0][0] == 0:
                    result = Q.popleft()
                else:
                    Q.append(Q.popleft())
                    Q[-1][0] = Q[-1][0] // 2
    print('#{} {}'.format(TC, result[1]))
