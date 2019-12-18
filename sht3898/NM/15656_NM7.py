import sys
sys.stdin = open('15656_input.txt', 'r')


def solve(k):
    if k == M:
        print(*arr)
        return
    for i in range(N):
        arr.append(numbers[i])
        solve(k+1)
        arr.pop()


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
arr = []
solve(0)
