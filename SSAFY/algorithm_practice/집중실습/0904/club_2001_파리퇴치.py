import sys; sys.stdin = open('2001_input.txt', 'r')
import pprint

for TC in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    temp = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    temp += arr[k][l]
            result = max(result, temp)
    print('#{} {}'.format(TC, result))
