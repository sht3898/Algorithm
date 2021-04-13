# import sys; sys.stdin = open('14502_input.txt', 'r')
# from collections import deque
# from itertools import combinations
# import copy
#
#
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
#
#
# def spread(board, visit):
#     Q = deque()
#     for x, y in virus:
#         Q.append([x, y])
#     while Q:
#         x, y = Q.popleft()
#         visit[x][y] = 1
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and board[nx][ny] != 1 and board[i][j] == 0:
#                 Q.append([nx, ny])
#                 board[nx][ny] = 2
#                 visit[nx][ny] = 1
#     return board
#
#
# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# bricks = []
# virus = []
# empty = []
# answer = 0
# for i in range(N):
#     for j in range(M):
#         if board[i][j] == 1:
#             bricks.append([i, j])
#         elif board[i][j] == 2:
#             virus.append([i, j])
#         else:
#             empty.append([i, j])
#
# for empty_list in list(combinations(empty, 3)):
#     visit = [[0] * M for _ in range(N)]
#     for x, y in empty_list:
#         board[x][y] = 1
#     temp_board = copy.deepcopy(board)
#     spread(board, visit)
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] == 0:
#                 cnt += 1
#     if cnt > answer:
#         print(empty_list)
#     answer = max(cnt, answer)
#     board = copy.deepcopy(temp_board)
#     for x, y in empty_list:
#         board[x][y] = 0
# print(answer)
import sys
a, b = sys.stdin.readline().split()
print(a, b)