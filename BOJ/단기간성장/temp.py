import sys; sys.stdin = open('12865_input.txt', 'r')

N, K = map(int, input().split())    # N: 물품의 수, K: 버틸 수 있는 무게
arr = [[0, 0]]
for _ in range(N):
    arr.append(list(map(int, input().split()))) # [무게, 가치]

knapsack = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        w = arr[i][0]
        v = arr[i][1]

        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(v+knapsack[i-1][j-w], knapsack[i-1][j])
print(knapsack[N][K])
