import sys; sys.stdin = open('15650_input.txt', 'r')

N, M = map(int, input().split())
arr = []
meet = [0] * N
result = []


def solve(k, n):
    if k == M:
        if sorted(arr) not in result:
            print(*sorted(arr))
            result.append(sorted(arr))
        return
    for i in range(n):
        if not meet[i]:
            meet[i] = 1
            arr.append(i+1)
            solve(k+1, n)
            arr.pop()
            meet[i] = 0


solve(0, N)
