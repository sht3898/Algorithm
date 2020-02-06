import sys
sys.stdin = open('14888_input.txt', 'r')


def solve(k, result, plus, minus, multiple, divide):
    global MAX, MIN
    if k == N:
        MAX = max(result, MAX)
        MIN = min(result, MIN)
        return
    if plus:
        solve(k+1, result + numbers[k], plus-1, minus, multiple, divide)
    if minus:
        solve(k+1, result - numbers[k], plus, minus-1, multiple, divide)
    if multiple:
        solve(k+1, result * numbers[k], plus, minus, multiple-1, divide)
    if divide:
        if result >= 0:
            solve(k+1, result//numbers[k], plus, minus, multiple, divide-1)
        elif result < 0:
            solve(k+1, -(-result//numbers[k]), plus, minus, multiple, divide-1)
    return


N = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))
MAX, MIN = -1e9, 1e9
solve(1, numbers[0], operator[0], operator[1], operator[2], operator[3])
print(MAX, MIN)
