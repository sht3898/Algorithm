import sys
sys.stdin = open('4869_input.txt', 'r')


def solve(n):
    if n == 1 or n == 2:
        return result[n]
    result[n] = solve(n-1) + solve(n-2) * 2
    return result[n]


for TC in range(1, int(input())+1):
    N = int(input()) // 10
    result = [0] * (N+1)
    result[1] = 1
    result[2] = 3
    print('#{} {}'.format(TC, solve(N)))
