import sys; sys.stdin = open('15650_input.txt', 'r')

N, M = map(int, input().split())
arr = []
meet = [0] * N


def solve(k, s):
    if k == M:
        print(*sorted(arr))
        return
    for i in range(s, N):
        if not meet[i]:
            meet[i] = 1
            arr.append(i+1)
            solve(k+1, i)
            arr.pop()
            meet[i] = 0


solve(0, 0)
