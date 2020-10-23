import sys; sys.stdin = open('5102_input.txt', 'r')
from collections import deque


def bfs(s, g):
    global result
    visit[s] = 1
    Q.append(s)
    while Q:
        temp = Q.popleft()
        for w in arr[temp]:
            if not visit[w]:
                visit[w] = 1
                Q.append(w)
                dist[w] = dist[temp] + 1
                if w == g:
                    result = dist[w]
                    return


for TC in range(1, int(input())+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    visit = [0] * (V+1)
    dist = [0] * (V+1)
    Q = deque()
    result = 0
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    S, G = map(int, input().split())
    bfs(S, G)
    print('#{} {}'.format(TC, result))

