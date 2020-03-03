import sys; sys.stdin = open('4864_input.txt', 'r')

for TC in range(1, int(input())+1):
    str1 = input()
    temp = list(str1)
    str2 = list(input())
    N, M = len(temp), len(str2)
    result = 0
    for i in range(M-N+1):
        temp = ''.join(str2[i:i+N])
        if str1 == temp:
            result = 1
            break
    print('#{} {}'.format(TC, result))
