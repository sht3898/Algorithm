def solution(begin, target, words):
    answer = 0
    n = len(words)
    visit = [0] * n

    def dfs(start, target, words):
        result = 0
        stack = [start]
        while stack:
            idx = stack.pop()
            if not visit[idx]:
                visit[idx] = 1
            for i in range(n):
                if not visit[i]:
                    cnt = 0
                    for j in range(len(words[i])):
                        if words[idx][j] != words[i][j]:
                            cnt += 1
                    if cnt == 1:
                        if words[i][j] == target:
                            return result
                        else:
                            result += 1
                            stack.append(i)

    for i, w in enumerate(words):
        if w == begin:
            print(dfs(i, target, words))
    return answer


print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))   # 4
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))  # 0
