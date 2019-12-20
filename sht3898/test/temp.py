import pprint
import sys
sys.stdin = open('2_input.txt', 'r')


# 깊이를 측정했는데 같은 깊이에 해당하는 값이 두개 이상이면 측정 불가
# 깊이를 탐색

from collections import deque


def bfs(v):
    Q = deque()
    Q.append(v)
    while Q:
        tmp = Q.popleft()
        for w in path[tmp]:
            temp[w] += 1
            Q.append(w)


for i in range(1, int(input())+1):
    N = int(input())
    M = int(input())
    board = [list(map(int, input().split())) for _ in range(M)]
    path = [[] for _ in range(N+1)]
    start = [0] * (N+1)
    depth = [0] * (N+1)
    for stu in board:
        a, b = stu[0], stu[1]
        path[a].append(b)
        start[b] += 1

    print(path)
    for s in range(1, len(start)):
        if start[s] == 0:
            temp = [0] * (N+1)
            bfs(s)
            for i in range(N+1):
                depth[i] = max(depth[i], temp[i])
            print(temp)
            print()
    # print(depth)
