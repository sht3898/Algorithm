import sys
sys.stdin = open('1931_input.txt', 'r')


def solve(arr):
    cnt = 0
    start = 0
    for meeting in arr:
        if meeting[0] >= start:
            start = meeting[1]
            cnt += 1
    return cnt


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x: x[0])
arr = sorted(arr, key=lambda x: x[1])
print(solve(arr))