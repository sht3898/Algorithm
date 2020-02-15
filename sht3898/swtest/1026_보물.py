import sys;
sys.stdin = open('1026_input.txt', 'r')


N = int(input())
a_list = sorted(list(map(int, input().split())), reverse=True)
b_list = sorted(list(map(int, input().split())))
result = 0
for i in range(N):
    result += a_list[i] * b_list[i]
print(result)
