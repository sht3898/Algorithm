import pprint
import sys
sys.stdin = open('14888_input.txt', 'r')


def solve(k, result, plus, minus, multi, div):
    global MAX, MIN
    if k == N:
        MAX = max(result, MAX)
        MIN = min(result, MIN)
        return
    if plus:
        solve(k+1, result + numbers[k], plus-1, minus, multi, div)
    if minus:
        solve(k+1, result - numbers[k], plus, minus - 1, multi, div)
    if multi:
        solve(k+1, result * numbers[k], plus, minus, multi-1, div)
    if div: # int(result/numbers[k])로 해야 음수일 때 정상적으로 나옴
        solve(k+1, int(result/numbers[k]), plus, minus, multi, div-1)
    return


N = int(input())
numbers = list(map(int, input().split()))
opers = list(map(int, input().split()))
MAX, MIN = -1e9, 1e9
solve(1, numbers[0], opers[0], opers[1], opers[2], opers[3])
print(MAX, MIN)
