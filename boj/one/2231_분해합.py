# import sys;
# sys.stdin = open('2231_input.txt', 'r')

N = int(input())
temp = 1
num = 0  # N의 10의 자리수 + 1
result = 1e9
while N >= temp:
    temp *= 10
    num += 1

if N-9*num >= 0:
    low = N - 9*num
else:
    low = 0

for i in range(low, N+1):
    sum_num = i
    temp = i
    while sum_num > 0:
        temp += sum_num % 10
        sum_num = sum_num // 10
    # temp += sum_num
    if temp == N:
        result = min(result, i)

if result == 1e9 or result < 10:
    print(0)
else:
    print(result)
