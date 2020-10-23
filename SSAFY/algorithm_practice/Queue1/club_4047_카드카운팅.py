import sys; sys.stdin = open('4047_input.txt', 'r')
from collections import deque

NUMS = ['0' + str(i) for i in range(1, 10)] + [str(i) for i in range(10, 14)]
S = ['S' + i for i in NUMS]
D = ['D' + i for i in NUMS]
H = ['H' + i for i in NUMS]
C = ['C' + i for i in NUMS]

for TC in range(1, int(input())+1):
    arr = input()
    Q = deque()
    result = [13, 13, 13, 13]
    check = 0
    while arr:
        temp = arr[:3]
        arr = arr[3:]
        if temp in Q:
            check = 1
            break
        Q.append(temp)

    if result != 'ERROR':
        for i in Q:
            if i in S:
                result[0] -= 1
            elif i in D:
                result[1] -= 1
            elif i in H:
                result[2] -= 1
            else:
                result[3] -= 1

    print('#{}'.format(TC), end=' ')
    if check:
        print('ERROR')
    else:
        print(*result)
