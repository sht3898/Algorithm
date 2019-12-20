import pprint
import sys
sys.stdin = open('2_input.txt', 'r')


# 깊이를 측정했는데 같은 깊이에 해당하는 값이 두개 이상이면 측정 불가
# 깊이를 탐색


def dfs(v):
    Q = []
    visit[v][v] = 1
    Q.append(v)
    while Q:
        temp = Q.pop()
        for w in path[temp]:
            if not visit[v][w]:
                visit[v][w] = 1
                visit[w][v] = 1
                Q.append(w)


for TC in range(1, int(input())+1):
    N = int(input())
    M = int(input())
    board = [list(map(int, input().split())) for _ in range(M)]
    visit = [[0] * (N+1) for _ in range(N+1)]
    path = [[] for _ in range(N+1)]
    result = 0
    for stu in board:
        a, b = stu[0], stu[1]
        path[a].append(b)

    for v in range(1, N+1):
        dfs(v)

    for i in range(1, N+1):
        if visit[i].count(1) == N:
            result += 1

    print('#{} {}'.format(TC, result))
# 서로 갈 수 있으면 비교 가능
# n*n 배열 만들고 1 -> 4 가능하면 [1, 4] [4, 1] 모두 true 로
