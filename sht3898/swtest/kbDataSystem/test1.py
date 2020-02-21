# 1차원 배열이 주어진후 배열 간의 거리가 가장 짧은 구간의 거리를 출력

import sys
sys.stdin = open('test1_input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
MIN = 1e9
for i in range(N-1):
    if abs(arr[i+1]-arr[i]) <= MIN:
        MIN = abs(arr[i+1] - arr[i])
print(MIN)
