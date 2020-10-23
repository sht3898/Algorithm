import sys; sys.stdin = open('1220_input.txt', 'r')

for TC in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        last = 0
        for i in range(N):
            if arr[i][j] == 1:
                last = 1
            elif arr[i][j] == 2:
                if last == 1:
                    cnt += 1
                    last = 0
    print('#{} {}'.format(TC, cnt))
