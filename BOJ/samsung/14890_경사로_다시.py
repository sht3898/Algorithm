import sys;sys.stdin = open('14890_input.txt', 'r')

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def check(line):
    for i in range(1, N):
        if abs(line[i-1] - line[i]) > 1:
            return False
        if line[i-1] > line[i]:
            for j in range(L):
                if i+j >= N or line[i] != line[i+j] or visited[i+j]:
                    return False
                if line[i] == line[i+j]:
                    visited[i+j] = 1
        elif line[i-1] < line[i]:
            for j in range(L):
                if i-j-1 < 0 or line[i-1] != line[i-j-1] or visited[i-j-1]:
                    return False
                if line[i-1] == line[i-j-1]:
                    visited[i-j-1] = 1
    return True


# 가로 확인
for i in range(N):
    visited = [0] * N
    if check([board[i][j] for j in range(N)]):
        answer += 1


# 세로 확인
for j in range(N):
    visited = [0] * N
    if check([board[i][j] for i in range(N)]):
        answer += 1

print(answer)
