import sys
sys.stdin = open('4881_input.txt', 'r')


def solve(SUM, i):
    global result
    if SUM >= result:
        return
    if i == N:
        result = min(result, SUM)
        return
    for j in range(N):
        if not visit[j]:
            visit[j] = 1
            solve(SUM+arr[i][j], i+1)
            visit[j] = 0


for TC in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    result = 0xfffff
    solve(0, 0)
    print('#{} {}'.format(TC, result))
