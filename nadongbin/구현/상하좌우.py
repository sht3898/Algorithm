# n = int(input())
# x, y = 1, 1
# plans = input().split()

n = 5
x, y = 1, 1
plans = ['R', 'R', 'R', 'U', 'D', 'D']

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny

print(nx, ny)