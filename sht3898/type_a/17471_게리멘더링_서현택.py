import sys
sys.stdin = open('17471_input.txt', 'r')

def back(k, n):
    pass


N = int(input())
populations = [0] + list(map(int, input().split()))
G = [[] for _ in range(N+1)]
for j in range(1, N+1):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)):
        G[j].append(tmp[i])

result = 1e9
A = []
back(1, N+1)    # 1에서 N 까지에 대한 부분집합을 생성

if result == 1e9:
    print(-1)
else:
    print(result)
