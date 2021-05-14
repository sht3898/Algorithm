import sys; sys.stdin = open('12015_input.txt', 'r')
import bisect

N = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(N):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))
