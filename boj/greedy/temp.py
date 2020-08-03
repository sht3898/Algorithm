import sys
sys.stdin = open('1931_input.txt', 'r')


def solve(arr):
    meeting_count = 0
    start_time = 0

    for time in arr:
        if time[0] >= start_time:
            start_time = time[1]
            meeting_count += 1
    return meeting_count


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x: x[0])
arr = sorted(arr, key=lambda x: x[1])
print(solve(arr))
