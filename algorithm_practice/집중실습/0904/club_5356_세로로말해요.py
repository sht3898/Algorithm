import sys; sys.stdin = open('5356_input.txt', 'r')

for TC in range(1, int(input())+1):
    arr = [list(input()) for _ in range(5)]
    result = ''
    MAX = 0
    for i in range(5):
        MAX = max(len(arr[i]), MAX)

    for j in range(MAX):
        for i in range(5):
            if len(arr[i]) > j:
                result += arr[i][j]

    print('#{} {}'.format(TC, result))
