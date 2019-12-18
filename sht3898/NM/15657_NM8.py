import sys
sys.stdin = open('15657_input.txt', 'r')


def solve(k, s):
    if k == M:
        print(*arr)
        return
    for i in range(s, N):
        arr.append(numbers[i])
        solve(k+1, i)
        arr.pop()


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
arr = []
solve(0, 0)
