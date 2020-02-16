import sys;
sys.stdin = open('7568_input.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ranks = []
for people in arr:
    rank = 1
    for i in range(N):
        if arr[i][0] > people[0] and arr[i][1] > people[1]:
            rank += 1
    ranks.append(rank)
print(*ranks)
