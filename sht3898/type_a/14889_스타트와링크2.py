import sys
sys.stdin = open('14889_input.txt', 'r')


def solve(k, s):
    global result
    if k == n:
        start, link = 0, 0
        x = list(set([x for x in range(N)]) - set(visit))
        for i in range(n - 1):
            for j in range(i+1, n):
                start += arr[visit[i]][visit[j]] + arr[visit[j]][visit[i]]
        for i in range(n - 1):
            for j in range(i+1, n):
                link += arr[x[i]][x[j]] + arr[x[j]][x[i]]
        result = min(result, abs(start - link))
    else:
        for i in range(s, N + k - n + 1):
            visit[k] = i
            solve(k+1, i+1)


N = int(input())
n = N // 2
visit = [0] * n
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0xfffff
solve(0, 0)
print(result)
