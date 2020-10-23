import sys
sys.stdin = open('4871_input.txt', 'r')


def dfs(v):
    visit[v] = 1
    for w in arr[v]:
        if not visit[w]:
            dfs(w)


for TC in range(1, int(input())+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    visit = [0] * (V + 1)
    for _ in range(E):
        U, V = map(int, input().split())
        arr[U].append(V)
    S, G = map(int, input().split())
    dfs(S)
    print('#{} {}'.format(TC, visit[G]))

