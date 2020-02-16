import sys
sys.stdin = open('1182_input.txt', 'r')


def solve(k, n):
    global cnt
    if k == n:
        if sorted(arr) not in result:
            result.append(sorted(arr))
            if sum(arr) == S:
                cnt += 1
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            arr.append(numbers[i])
            solve(k+1, n)
            arr.pop()
            visit[i] = 0


N, S = map(int, input().split())
numbers = list(map(int, input().split()))
result = []
arr = []
visit = [0] * N
cnt = 0
for i in range(1, N+1):
    solve(0, i)
print(cnt)
