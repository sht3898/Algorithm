import sys
sys.stdin = open('3_input.txt', 'r')

import itertools

for TC in range(1, int(input())+1):
    N, x, y = map(int, input().split())
    result = -1
    arr = []
    numbers = []
    arr.append(x)
    arr.append(y)
    numbers.append(list(itertools.permutations(arr, 2)))
    print(numbers)
