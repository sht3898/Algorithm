from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[0]*n for _ in range(n)]
    dist = [0]*n
    visit = [0]*n
    Q = deque([0])
    visit[0] = 1
    for s, e in edge:
        graph[s-1].append(e-1)
        graph[e-1].append(s-1)
    while Q:
        s = Q.popleft()
        for e in graph[s]:
            if not visit[e]:
                visit[e] = 1
                Q.append(e)
                dist[e] = dist[s] + 1
    dist.sort(reverse=True)
    answer = dist.count(dist[0])
    return answer


def solution2(n, edge):
    answer = 0
    graph = dict()
    for s, e in edge:
        if s not in graph:
            graph[s] = [e]
        else:
            graph[s].append(e)

        if e not in graph:
            graph[e] = [s]
        else:
            graph[e].append(s)
    Q = deque()
    Q.append([1, 0])
    visit = [-1]*(n+1)
    while Q:
        s, cnt = Q.popleft()
        visit[s] = cnt
        for e in graph[s]:
            if visit[e] == -1:
                visit[e] = 0
                Q.append([e, cnt+1])
        cnt += 1
    answer = visit.count(max(visit))
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 3
