import sys
sys.stdin = open('11047_input.txt', 'r')

N, K = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)], reverse=True)
idx = 0
tmp = 0
cnt = 0
while tmp != K:
    if tmp + arr[idx] > K:
        idx += 1
    elif tmp + arr[idx] <= K:
        tmp += arr[idx]
        cnt += 1
print(cnt)
