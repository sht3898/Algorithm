import sys; sys.stdin = open('1267_input.txt', 'r')
from collections import deque


def bfs(graph):
    for i in range(1, V+1):
        if depth[i] == 0:
          Q.append(i)
    while Q:
        temp = Q.popleft()
        result.append(temp)
        for w in graph[temp]:
            if depth[w] != 0:
                depth[w] -= 1
                if depth[w] == 0:
                    Q.append(w)


for TC in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[] for _ in range(V+1)]
    depth = [0] * (V+1)
    Q = deque()
    result = []
    for i in range(len(arr)//2):
        G[arr[2*i]].append(arr[2*i+1])
        depth[arr[2*i+1]] += 1
    bfs(G)
    print('#{}'.format(TC), end=' ')
    print(*result)
