from collections import deque


def solution(m, n, puddles):
    dp = [[1] * m for _i in range(n)]

    for x, y in puddles:
        dp[y - 1][x - 1] = 0
        if x - 1 == 0:
            for k in range(y - 1, n):
                dp[k][0] = 0
        if y - 1 == 0:
            for k in range(x - 1, m):
                dp[0][k] = 0

    for i in range(1, n):
        for j in range(1, m):
            if i * j != 0:
                if dp[i][j] != 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    answer = dp[n - 1][m - 1]
    return answer % 1000000007

def solution2(m, n, puddles):
    answer = 0
    result = 0
    board = [[0] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    for x, y in puddles:
        board[x][y] = -1

    def bfs(x, y):
        nonlocal result
        Q = deque()
        visit[x][y] = 1
        Q.append((x, y))
        while Q:
            x, y = Q.popleft()
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and board[nx][ny] != -1:
                    visit[nx][ny] = 1
                    Q.append((nx, ny))
                    if nx == n - 1 and ny == m - 1:
                        result += 1

    bfs(0, 0)
    print(result)
    return answer


print(solution(4, 3, [[2, 2]]))   # 4
