import sys
sys.stdin = open('1865_input.txt', 'r')


def solve(k):
    global sub_result, result

    if sub_result <= result:
        return

    if k == N:
        result = sub_result
        return

    for j in range(N):
        if not visit[j]:
            if arr[k][j] == 0:
                continue
            else:
                sub_result *= (arr[k][j]/100)
                visit[j] = 1
                solve(k+1)
                sub_result /= (arr[k][j]/100)
                visit[j] = 0


for TC in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    sub_result, result = 1, 0
    solve(0)
    print('#{0} {1:.6f}'.format(TC, round(result*100, 6)))
