# N과 M 사이의 숫자 중 자연수의 제곱인 수의 집합을 구하고
# 집합에서의 최소값과 집합의 합을 출력

import sys
sys.stdin = open('test2_input.txt', 'r')

import math
N, M = map(int, input().split())
results = []
n, m = math.ceil(math.sqrt(N)), math.floor(math.sqrt(M))
for i in range(n, m+1):
    results.append(i*i)
print(min(results), sum(results))
