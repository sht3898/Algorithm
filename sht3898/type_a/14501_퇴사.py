import sys
sys.stdin = open('14501_input.txt', 'r')


def solve(date, money):
    global ans
    if date == N:
        ans = max(ans, money)
        return
    if T[date] <= N - date:
        solve(date + T[date], money + P[date])
    solve(date + 1, money)


N = int(input())
T, P = [], []
ans = 0

for _ in range(N):
    tmp1, tmp2 = map(int, input().split())
    T.append(tmp1)
    P.append(tmp2)
solve(0, 0)
print(ans)
