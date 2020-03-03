import sys; sys.stdin = open('4865_input.txt', 'r')

for TC in range(1, int(input())+1):
    str1, str2 = list(input()), list(input())
    result = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
                if cnt > result:
                    result = cnt
    print('#{} {}'.format(TC, result))
