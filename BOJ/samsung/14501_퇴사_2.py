import sys; sys.stdin = open('14501_input.txt', 'r')

N = int(input())
T, P = [0]*N, [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())
dp = [0] * 20
for i in range(N):
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]
    if dp[i+T[i]] < dp[i] + P[i]:
        dp[i+T[i]] = dp[i]+P[i]
print(dp[N])
