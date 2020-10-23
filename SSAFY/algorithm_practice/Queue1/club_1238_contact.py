import sys; sys.stdin = open('1238_input.txt', 'r')
from collections import deque


def bfs(s):
    visit[s] = 1
    Q.append(s)
    while Q:
        temp = Q.popleft()
        for w in G[temp]:
            if not visit[w]:
                visit[w] = 1
                Q.append(w)
                depth[w] = depth[temp] + 1


for TC in range(1, 11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[] * (N+1) for _ in range(N+1)]
    visit = [0] * (N+1)
    depth = [0] * (N+1)
    Q = deque()
    result = 0
    for i in range(len(arr)//2):
        G[arr[2*i]].append(arr[2*i+1])

    bfs(S)

    for i in range(N+1):
        if depth[i] == max(depth):
            result = i
    print('#{} {}'.format(TC, result))

