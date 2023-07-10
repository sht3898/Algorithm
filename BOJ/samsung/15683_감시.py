import sys; sys.stdin = open('15683_input.txt', 'r')

N, M = map(int, input().split())
check = [[0] * M for _ in range(N)]
board = []
wall = []
camera = []
# one = []
# two = []
# three = []
# four = []
# five = []

for i in range(N):
    x = list(map(int, input().split()))
    for j, y in enumerate(x):
        if y == 6:
            wall.append([i, j])
        elif y != 0:
            camera.append([y, i, j])
        # elif y == 1:
        #     one.append([i, j])
        # elif y == 2:
        #     two.append([i. j])
        # elif y == 3:
        #     three.append([i, j])
        # elif y == 4:
        #     four.append([i, j])
        # elif y == 5:
        #     five.append([i, j])
    board.append(x)

print(N, M)
print(board)
print(wall)
print(camera)
