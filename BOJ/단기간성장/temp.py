import sys; sys.stdin = open('12865_input.txt', 'r')

N, K = map(int, input().split())
bag = [[0] * (K+1) for _ in range(N+1)]
arr = [[0, 0]]
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        w = arr[i][0]
        v = arr[i][1]

        if w > j:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(v+bag[i-1][j-w], bag[i-1][j])
print(bag[N][K])
