import sys; sys.stdin = open('4836_input.txt', 'r')

for TC in range(1, int(input())+1):
    N = int(input())
    rectangles = [list(map(int, input().split())) for _ in range(N)]
    maps = [[0] * 10 for _ in range(10)]
    cnt = 0
    for rectangle in rectangles:
        r1, c1, r2, c2, color = (rectangle[x] for x in range(0, 5))
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                maps[x][y] += color
                if maps[x][y] == 3:
                    cnt += 1
    print('#{} {}'.format(TC, cnt))
