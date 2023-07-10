import sys;
sys.stdin = open('14891_input.txt', 'r')

import copy

def self_rotate(line, d):
    temp_line = copy.deepcopy(line)
    if d == 1:
        for i in range(8):
            line[i] = temp_line[i-1]
    elif d == -1:
        for i in range(8):
            line[i] = temp_line[(i+1)%8]
    return line

def right_rotate(before, after, d):
    if before[2] == after[7]:
        return after, d, 1
    elif before[2] != after[7]:
        return self_rotate(after, d*(-1)), d*(-1), 0

def left_rotate(before, after, d):
    if before[7] == after[2]:
        return after, d, 1
    elif before[7] != after[2]:
        return self_rotate(after, d*(-1)), d*(-1), 0

answer = 0
first = list(map(int, list(input())))
second = list(map(int, list(input())))
third = list(map(int, list(input())))
forth = list(map(int, list(input())))
K = int(input())
for _ in range(K):
    num, d = map(int, input().split())
    left_d, right_d = d, d
    stop = 0
    if num == 1:
        first = self_rotate(first, d)
        second, right_d, stop = right_rotate(first, second, right_d)
        if stop==1: continue
        third, right_d, stop = right_rotate(second, third, right_d)
        if stop==1: continue
        forth, right_d, stop = right_rotate(third, forth, right_d)
    elif num == 2:
        second = self_rotate(second, d)
        first, left_d, stop = left_rotate(second, first, d)
        third, right_d, stop = right_rotate(second, third, right_d)
        if stop==1: continue
        forth, right_d, stop = right_rotate(third, forth, right_d)
    elif num == 3:
        third = self_rotate(third, d)
        forth, right_d, stop = right_rotate(third, forth, right_d)
        second, left_d, stop = left_rotate(third, second, left_d)
        if stop==1: continue
        first, left_d, stop = left_rotate(second, first, left_d)
    else:
        forth = self_rotate(forth, d)
        third, left_d, stop = left_rotate(forth, third, left_d)
        if stop==1: continue
        second, left_d, stop = left_rotate(third, second, left_d)
        if stop==1: continue
        first,left_d, stop = left_rotate(second, first, left_d)


if first[0] == 1:
    answer += 1
if second[0] == 1:
    answer += 2
if third[0] == 1:
    answer += 4
if forth[0] == 1:
    answer += 8

print(answer)
