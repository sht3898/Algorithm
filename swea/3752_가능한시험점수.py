import sys
sys.stdin = open('3752_input.txt', 'r')


# 내 풀이
def solve(k, s):
    if k == N:
        result.add(s)
        return
    if visit[k][s]:
        return
    else:
        visit[k][s] = 1
        solve(k+1, s+arr[k])
        solve(k+1, s)


for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    visit = [[0] * 10000 for _ in range(N)]
    result = set()
    solve(0, 0)
    print('#{0} {1}'.format(TC, len(result)))

# 무무형 풀이
for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = set({0})
    for i in range(N):
        tmp = set()
        for n in result:
            tmp.add(n+arr[i])
        result = result | tmp
    print('#{0} {1}'.format(TC, len(result)))

# 진희 누나 풀이
for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = set({0})
    for i in arr:
        tmp = set()
        for n in result:
            tmp.add(n+i)
        result = result.union(tmp)
    print('#{} {}'.format(TC, len(result)))
