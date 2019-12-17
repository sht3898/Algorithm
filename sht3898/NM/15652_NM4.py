import sys
sys.stdin = open('15652_input.txt', 'r')


def solve(k, s):
    if k == M:
        print(*arr)
        return
    for i in range(s+1, N+1):
        arr.append(i)
        solve(k+1, i-1)
        arr.pop()


N, M = map(int, input().split())
arr = []
solve(0, 0)
