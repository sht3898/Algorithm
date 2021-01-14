import sys; sys.stdin = open('12865_input.txt', 'r')

N, K = map(int, input().split())
arr = [[0, 0]]
for _ in range(N):
    arr.append(list(map(int, input().split())))
bag = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1): # i: 물건 번호
    for j in range(1, K+1): # j: 가방 최대 무게
        weight = arr[i][0]
        value = arr[i][1]

        if weight > j:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(value+bag[i-1][j-weight], bag[i-1][j])

print(bag[N][K])
