import sys; sys.stdin = open('10816_input.txt', 'r')

N = int(sys.stdin.readline())
board = list(map(int, sys.stdin.readline().split()))
M = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dic = {}
for num in board:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
print(*(dic[i] if i in dic else 0 for i in arr))
