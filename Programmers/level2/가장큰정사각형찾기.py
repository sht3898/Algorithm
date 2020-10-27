def solution(board):
    # DP 방식이라는데 잘 이해가 가지 않음
    width = len(board[0])
    height = len(board)
    for x in range(1,height):
        for y in range(1,width):
            if board[x][y] == 1:
                board[x][y] = min(board[x-1][y-1], min(board[x-1][y], board[x][y-1])) + 1
    return max([item for row in board for item in row])**2


def solution_fail(board):
    answer = -1e9
    N = len(board)

    def search(x, y, N, M):
        height_cnt = 0
        width_cnt = 0
        for n in range(x, N):
            if board[n][y]:
                height_cnt += 1
        for n in range(y, M):
            if board[x][y]:
                width_cnt += 1
        return height_cnt, width_cnt

    def area(start_x, start_y, end_x, end_y):
        cnt = 0
        for i in range(start_x, start_x + end_x):
            for j in range(start_y, start_y + end_y):
                if board[i][j] == 0:
                    return 0
                else:
                    cnt += 1
        return cnt

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                x, y = search(i, j, len(board), len(board[i]))
                new_area = area(i, j, x, y)
                answer = max(answer, new_area)
    return answer


if __name__ == '__main__':
    print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))  # 9
    print(solution([[0,0,1,1],[1,1,1,1]]))  # 4
