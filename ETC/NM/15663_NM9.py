import sys
sys.stdin = open('15663_input.txt', 'r')

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visit = [0] * N
arr = []
result = []


def solve(k):
    if k == M:
        tmp = ' '.join(map(str, arr))
        if tmp not in result:
            result.append(tmp)
            print(tmp)
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            arr.append(numbers[i])
            solve(k+1)
            visit[i] = 0
            arr.pop()


solve(0)
