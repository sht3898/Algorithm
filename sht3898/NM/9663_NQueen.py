import pprint
import sys
sys.stdin = open('9663_input.txt', 'r')


def promising(k):
    for i in range(k):
        if row[i] == row[k] or abs(row[i] - row[k]) == abs(i - k):
            return False
    return True


def solve(k):
    global result
    if k == N:
        result += 1
        tmp = ' '.join(map(str, arr))
        ans.append(tmp)
        return
    for i in range(N):
        row[k] = i
        if promising(k):
            arr.append(i)
            solve(k+1)
            arr.pop()


N = int(input())
row = [0] * N   # 행
arr = []
ans = []
result = 0
solve(0)
print(result)
