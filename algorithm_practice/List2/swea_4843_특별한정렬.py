import sys; sys.stdin = open('4843_input.txt', 'r')

for TC in range(1, int(input())+1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    n = len(arr)
    result = []
    while arr:
        result.append(arr.pop())
        result.append(arr.pop(0))
    print('#{}'.format(TC), end=' ')
    print(*result[:10])
