import sys
# sys.stdin = open('1065_input.txt', 'r')

N = int(input())
result = 0
for i in range(1, N+1):
    cnt = 0
    num_list = []
    tmp = i
    while tmp > 0:
        num_list.append(tmp % 10)
        tmp //= 10
    if len(num_list) >= 3:
        idx = 0
        while idx < len(num_list) - 2:
            if num_list[idx+2] - num_list[idx+1] == num_list[idx+1] - num_list[idx]:
                idx += 1
            else:
                break
        if idx == len(num_list) - 2:
            cnt += 1
    else:
        cnt = 1
    result += cnt
print(result)
