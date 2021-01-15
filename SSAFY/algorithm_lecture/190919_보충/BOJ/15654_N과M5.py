import sys; sys.stdin = open('15654_input.txt', 'r')

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)
meet = [0] * 10001
arr = []


def solve(k):
    if k == M:
        print(*arr)
        return
    for i in range(len(numbers)):
        num = numbers[i]
        if not meet[num]:
            meet[num] = 1
            arr.append(num)
            solve(k+1)
            meet[num] = 0
            arr.pop()


solve(0)
