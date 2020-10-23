import sys; sys.stdin = open('4834_input.txt', 'r')

for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input()))
    numbers = [0] * 10
    result = 0
    MAX = 0
    for num in arr:
        numbers[num] += 1
    for i in range(len(numbers)):
        if result <= numbers[i]:
            result = numbers[i]
            MAX = i
    print('#{} {} {}'.format(TC, MAX, result))
