def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    board = {1: (0, 0), 2: (0, 1), 3: (0, 2),
             4: (1, 0), 5: (1, 1), 6: (1, 2),
             7: (2, 0), 8: (2, 1), 9: (2, 2),
             '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = number
        elif number in [3, 6, 9]:
            answer += 'R'
            right = number
        else:
            left_hand = board[left]
            right_hand = board[right]
            now = board[number]
            if abs(left_hand[0] - now[0]) + abs(left_hand[1] - now[1]) < abs(right_hand[0] - now[0]) + abs(right_hand[1] - now[1]):
                answer += 'L'
                left = number
            elif abs(left_hand[0] - now[0]) + abs(left_hand[1] - now[1]) > abs(right_hand[0] - now[0]) + abs(right_hand[1] - now[1]):
                answer += 'R'
                right = number
            else:
                if hand == 'left':
                    answer += 'L'
                    left = number
                else:
                    answer += 'R'
                    right = number
    return answer


if __name__ == '__main__':
    # print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
