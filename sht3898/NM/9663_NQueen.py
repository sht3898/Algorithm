import pprint
import sys
sys.stdin = open('9663_input.txt', 'r')


def promising(i):
    for j in range(0, i):
        # 새로운 퀸과 기존의 퀸이 같은 행에 있거나 대각선에 있을 경우
        if row[j] == row[i] or abs(row[j] - row[i]) == (i - j):
            return False
    return True


def n_queen(i):
    global result
    if i == N:
        result += 1
    else:
        for j in range(N):
            row[i] = j
            if promising(i):
                n_queen(i + 1)


N = int(input())
row = [0] * N
result = 0
n_queen(0)
print(result)
