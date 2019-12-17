import sys
sys.stdin = open('15655_input.txt', 'r')


def solve(k, s):
    if k == M:
        print(*arr)
        return
    for i in range(s, N):
        if not visit[i]:
            visit[i] = 1
            arr.append(numbers[i])
            solve(k+1, i)
            arr.pop()
            visit[i] = 0


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visit = [0] * N
arr = []
solve(0, 0)
