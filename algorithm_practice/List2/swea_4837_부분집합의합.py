import sys; sys.stdin = open('4837_input.txt', 'r')

for TC in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = list(range(1, 13))
    n = len(arr)
    cnt = 0
    for i in range(1 << n):
        result = []
        for j in range(n):
            if i & (1 << j):
                result.append(arr[j])
        if len(result) == N and sum(result) == K:
            cnt += 1
    print('#{} {}'.format(TC, cnt))
