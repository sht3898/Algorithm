def solution(board, moves):
    answer = 0
    N = len(board)
    bag = []
    for move in moves:
        for i in range(N):
            if board[i][move-1]:
                print(i, move-1)
                bag.append(board[i][move-1])
                board[i][move-1] = 0
                if len(bag) >= 2:
                    if bag[-1] == bag[-2]:
                        bag.pop()
                        bag.pop()
                        answer += 2
                break
    return answer