import sys
sys.stdin = open('15649_input.txt', 'r')


def solve(k, n):
    if k == M:
        print(*arr)
        return
    for i in range(1, n+1):
        if not visit[i]:
            visit[i] = 1
            arr.append(i)
            solve(k+1, n)
            arr.pop()
            visit[i] = 0


N, M = map(int, input().split())
visit = [0] * (N+1)
arr = []
solve(0, N)
