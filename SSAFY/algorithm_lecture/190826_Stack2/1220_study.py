import sys; sys.stdin = open('1220_input.txt', 'r')


for TC in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for j in range(N):
        meet = 0
        for i in range(N):
            if arr[i][j] == 0:
                continue
            elif arr[i][j] == 1:
                meet = 1
            elif meet == 1 and arr[i][j] == 2:
                count += 1
                meet = 0
            elif meet == 0 and arr[i][j] == 2:
                continue
    print('#{} {}'.format(TC, count))
