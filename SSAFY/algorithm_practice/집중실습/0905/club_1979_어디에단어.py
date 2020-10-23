import sys; sys.stdin = open('1979_input.txt', 'r')
import pprint


def is_possible(i):
    global j

    idx = 0
    while j + idx < N and arr[i][j + idx]:
        idx += 1
    j = j + idx
    if idx == K:
        return True
    else:
        return False


for TC in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        j = 0
        while j < N - K + 1:
            if arr[i][j] and is_possible(i):
                result += 1
            j += 1

    for i in range(N):
        for j in range(i, N):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(N):
        j = 0
        while j < N - K + 1:
            if arr[i][j] and is_possible(i):
                result += 1
            j += 1

    print('#{} {}'.format(TC, result))
