# import sys; sys.stdin = open('1493_input.txt', 'r')
import sys; sys.stdin = open('temp.txt', 'r')
import pprint


for TC in range(1, int(input())+1):
    p, q = map(int, input().split())
    # arr = [[0] * 10001 for _ in range(10001)]
    arr = [[0] * 11 for _ in range(11)]
    N = len(arr)
    arr[1][1] = 1
    for i in range(1, N):
        for j in range(1, N):
            if i == 1 and j == 1:
                continue
            arr[i][j] = arr[i-1][j-1] + i + j
    pprint.pprint(arr)