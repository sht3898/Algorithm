import sys
sys.stdin = open('14889_input.txt', 'r')

def solve(k, s):
    global result
    if k == L:
        return
    else:
        



N = int(input())
L = N // 2
S = [list(map(int, input().split())) for _ in range(N)]
result = 1e9
print(S)