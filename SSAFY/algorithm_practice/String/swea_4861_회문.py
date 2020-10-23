import sys; sys.stdin = open('4861_input.txt', 'r')

for TC in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = ''
    for i in range(N):
        for j in range(N-M+1):
            temp = []
            temp2 = []
            for k in range(M):
                temp.append(arr[i][j+k])
                temp2.append(arr[j+k][i])
            if temp == temp[::-1]:
                result = temp
            if temp2 == temp2[::-1]:
                result = temp2
    print('#{} {}'.format(TC, ''.join(result)))
