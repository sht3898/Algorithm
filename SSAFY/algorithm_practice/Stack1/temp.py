import sys; sys.stdin = open('1267_input.txt', 'r')
from collections import deque


def bfs(graph):
    for i in range(1, V+1):
        if degree[i] == 0:
            start = i
            Q.append(start)
    while Q:
        temp = Q.popleft()
        result.append(temp)
        for w in graph[temp]:
            if degree[w] != 0:
                degree[w] -= 1
                if degree[w] == 0:
                    Q.append(w)


for TC in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(V+1)]
    degree = [0] * (V+1)
    visit = [0] * (V+1)
    Q = deque()
    result = []
    for i in range(len(arr)//2):
        graph[arr[2*i]].append(arr[2*i+1])
        degree[arr[2*i+1]] += 1
    bfs(graph)
    print('#{} {}'.format(TC, ' '.join(list(map(str, result)))))
