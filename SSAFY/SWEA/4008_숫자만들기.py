import sys;
sys.stdin = open('4008_input.txt', 'r')


def solve(k, plus, minus, multiple, divide, s):
    global MAX, MIN
    if k == N:
        MAX = max(MAX, s)
        MIN = min(MIN, s)
    else:
        if plus:
            solve(k+1, plus-1, minus, multiple, divide, s+numbers[k])
        if minus:
            solve(k+1, plus, minus-1, multiple, divide, s-numbers[k])
        if multiple:
            solve(k+1, plus, minus, multiple-1, divide, s*numbers[k])
        if divide:
            if s >= 0:
                solve(k+1, plus, minus, multiple, divide-1, s // numbers[k])
            elif s < 0:
                solve(k+1, plus, minus, multiple, divide-1, -(-s // numbers[k]))


for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))   # +, -, *, / 개수
    numbers = list(map(int, input().split()))   # 주어진 숫자
    MAX = -1e9
    MIN = 1e9
    solve(1, arr[0], arr[1], arr[2], arr[3], numbers[0])
    # solve(0, arr[0], arr[1], arr[2], arr[3], 0)
    print('#{} {}'.format(TC, MAX - MIN))
