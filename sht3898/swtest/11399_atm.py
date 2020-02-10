import sys
sys.stdin = open('11399_input.txt', 'r')


def solve(times):
    total_time = 0
    waiting_time = 0
    times.sort()
    for time in times:
        waiting_time += time
        total_time += waiting_time
    return total_time


N = int(input())
arr = sorted(list(map(int, input().split())))
print(solve(arr))
