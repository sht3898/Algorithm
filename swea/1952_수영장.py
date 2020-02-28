import sys
sys.stdin = open('1952_input.txt', 'r')


def solve(k, s):
    global MIN
    if k >= 13:
        MIN = min(MIN, s)
    else:
        solve(k+1, s+fees[0]*plans[k])
        solve(k+1, s+fees[1])
        solve(k+3, s+fees[2])


for TC in range(1, int(input())+1):
    fees = list(map(int, input().split()))
    plans = [0] + list(map(int, input().split()))
    MIN = fees[3]
    solve(1, 0)
    print('#{} {}'.format(TC, MIN))
