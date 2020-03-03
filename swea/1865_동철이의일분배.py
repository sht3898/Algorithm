import sys
sys.stdin = open('1865_input.txt', 'r')


def solve(k, n):
    return


for TC in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    answer = 1
    for i in range(N):
        visit[i] = 1
