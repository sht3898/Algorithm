import sys
sys.stdin = open('ex1_input.txt', 'r')

N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
MIN = min(arr)
idx = 0
while sum(arr) != MIN * N:
	small_MIN = min(arr[idx:idx+K])
	for i in range(idx, idx+K):
		if arr[i] > small_MIN:
			arr[i] = small_MIN
	idx = (idx+1) % (N-1)
	cnt += 1
print(cnt)