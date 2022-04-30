import sys; sys.stdin = open('5658_input.txt', 'r')

for T in range(1, int(input())+1):
    N, K = map(int, input().split())
    d_num = N // 4
    numbers = input()
    num_set = set()
    for _ in range(d_num):
        first = int(numbers[:d_num], 16)
        second = int(numbers[d_num:d_num*2], 16)
        third = int(numbers[d_num*2:d_num*3], 16)
        forth = int(numbers[d_num*3:], 16)
        num_set.add(first)
        num_set.add(second)
        num_set.add(third)
        num_set.add(forth)
        numbers = numbers[-1] + numbers[:-1]
    print('#{} {}'.format(T, sorted(num_set, reverse=True)[K-1]))
