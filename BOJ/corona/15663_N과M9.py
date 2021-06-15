import sys; sys.stdin = open('15663_input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())
a = sorted(list(map(int, sys.stdin.readline().split())))
result = []
visit = [0] * n
s = []


def f(k):
    if k == m:
        temp = ' '.join(map(str, s))
        if temp not in result:
            print(temp)
            result.append(temp)
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            s.append(a[i])
            f(k+1)
            s.pop()
            visit[i] = 0
f(0)
