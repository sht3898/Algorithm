import sys; sys.stdin = open('6190_input.txt', 'r')


def solve(array):
    for num in sorted(array, reverse=True):
        tmp = num
        for i in range(len(str(num))-1):
            if str(num)[i] > str(num)[i+1]:
                tmp = 0
                break
        if tmp > 0:
            return num
    return -1


for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    numbers = []
    MAX = 0
    for i in range(N):
        for j in range(i):
            numbers.append(arr[i] * arr[j])
    print('#{} {}'.format(TC, solve(numbers)))
