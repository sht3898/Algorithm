import sys; sys.stdin = open('3190_input.txt', 'r')
from collections import deque

N = int(input())
game = [[0 for _ in range(N+1)] for _ in range(N+1)]
K = int(input())
snake = [[1, 1]]
time = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
c = []

for _ in range(K):
    x, y = map(int, input().split())
    game[x][y] = 1

p = int(input())
s = [0 for _ in range(p+1)]

for i in range(p):
    x, y = list(input().split())
    s[i] = x
    c.append(y)

x=1
y=1
j=0
head=0
while snake:
    x = x+dx[head]
    y = y+dy[head]
    time += 1

    if [x, y] in snake or x < 1 or y < 1 or x > N or y > N:
        break
    if game[x][y] == 0:
        snake.append([x, y])
        del snake[0]
    elif game[x][y] == 1:
        snake.append([x, y])
        game[x][y] = 0

    if int(s[j]) == time:
        if c[j] == 'D':
            head += 1
        elif c[j] == 'L':
            head -= 1
        j += 1

    if head == 4 or head == -4:
        head = 0
print(time)
