import sys
sys.stdin = open('2819_input.txt', 'r')


def solve(x, y, tmp, k):
    if k == 7:
        result.add(tmp)
        return
    else:
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                solve(nx, ny, tmp + board[nx][ny], k+1)


for TC in range(1, int(input())+1):
    board = [list(input().split()) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            solve(i, j, board[i][j], 1)
    print('#{} {}'.format(TC, len(result)))
