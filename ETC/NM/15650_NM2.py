import sys
sys.stdin = open('15650_input.txt', 'r')


def solve(k, s):
    if k == M:
        print(*arr)
        return
    for i in range(s+1, N+1):
        if not visit[i]:
            visit[i] = 1
            arr.append(i)
            solve(k+1, i)
            arr.pop()
            visit[i] = 0


N, M = map(int, input().split())
arr = []
visit = [0] * (N+1)
solve(0, 0)
