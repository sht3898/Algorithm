import sys; sys.stdin = open('14890_input.txt', 'r')


def garo(i):
    c = [0] * N
    for j in range(N-1):
        if abs(board[i][j] - board[i][j+1]) > 1:
            return 0

        if board[i][j] < board[i][j+1]:
            temp = [0] * N
            for k in range(L):
                if j - k < 0:
                    return 0
                if board[i][j] != board[i][j-k] or c[j-k] != 0:
                    return 0
                temp[j-k] = 1
            c = temp
        elif board[i][j] > board[i][j+1]:
            temp = [0]*N
            for k in range(L):
                if j + k + L >= N:
                    return 0
                if board[i][j+1] != board[i][j+k+1] or c[j+k+1] != 0:
                    return 0
                temp[j+k+1] = 1
            c = temp
        return 1


def sero(j):
    c = [0 for _ in range(N)]
    for i in range(N-1):
        if abs(board[i][j] - board[i + 1][j]) > 1:
            return 0

        if board[i][j] < board[i + 1][j]:
            temp = [0 for _ in range(N)]
            for k in range(L):
                if i - k < 0:
                    return 0
                if board[i][j] != board[i - k][j] or c[i - k] != 0:
                    return 0
                temp[i - k] = 1
            c = temp

        elif board[i][j] > board[i + 1][j]:
            temp = [0 for _ in range(N)]
            for k in range(L):
                if i + k + 1 >= N:
                    return 0
                if board[i + 1][j] != board[i + k + 1][j] or c[i + k + 1] != 0:
                    return 0
                temp[i + k + 1] = 1
            c = temp
    return 1


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for i in range(N):
    answer += garo(i)
    answer += sero(i)
print(answer)
