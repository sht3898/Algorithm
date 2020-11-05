def solution(n, computers):
    answer = 0
    visit = [0] * n

    def dfs(start):
        stack = [start]
        while stack:
            idx = stack.pop()
            if visit[idx] == 0:
                visit[idx] = 1
            for i in range(n):
                if computers[idx][i] == 1 and not visit[i]:
                    stack.append(i)

    i = 0
    while 0 in visit:
        if visit[i] == 0:
            dfs(i)
            answer += 1
        i += 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))   # 1
