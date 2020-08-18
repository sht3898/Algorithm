def solution(numbers, hand):
    answer = ''
    left_hand = 10
    right_hand = 12

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left_hand = number
        elif number in [3, 6, 9]:
            answer += 'R'
            right_hand = number
        else:
            if abs(int(left_hand) - int(number)) > abs(int(right_hand) - int(number)):
                answer += 'R'
                right_hand = number
            elif abs(int(left_hand) - int(number)) < abs(int(right_hand) - int(number)):
                answer += 'L'
            else:
                if hand == 'right':
                    answer += 'R'
                    right_hand = 'R'
                else:
                    answer += 'L'
                    left_hand = 'L'
    return answer


if __name__ == '__main__':
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))



# def solution(numbers, hand):
#     answer = ''
#     board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
#     left_hand = [3, 0]
#     right_hand = [3, 2]
#
#     def solve(i, j, dist, num):
#         for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
#             nx, ny = i + dx, j + dy
#             if 0 <= nx < 4 and 0 <= ny < 3 and not visit[nx][ny]:
#                 if board[nx][ny] == num:
#                     return dist
#                 else:
#                     visit[nx][ny] = 1
#                     solve(nx, ny, dist+1, num)
#
#     def location(num):
#         for i in range(4):
#             for j in range(3):
#                 if num == board[i][j]:
#                     return [i, j]
#
#     for number in numbers:
#         if number in [1, 4, 7]:
#             answer += 'L'
#             left_hand = location(number)
#         elif number in [3, 6, 9]:
#             answer += 'R'
#             right_hand = location(number)
#         else:
#             if solve(left_hand[0], left_hand[1], 0, number) < solve(right_hand[0], right_hand[1], 0, number):
#                 answer += 'L'
#                 left_hand = location(number)
#             elif solve(left_hand[0], left_hand[1], 0, number) > solve(right_hand[0], right_hand[1], 0, number):
#                 answer += 'R'
#                 right_hand = location(number)
#             else:
#                 if hand == 'left':
#                     answer += 'L'
#                     left_hand = location(number)
#                 else:
#                     answer += 'R'
#                     right_hand = location(number)
#
#
# if __name__ == '__main__':
#     print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
