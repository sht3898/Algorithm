import sys; sys.stdin = open('4835_input.txt', 'r')

for TC in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sums = []
    for i in range(N-M+1):
        sums.append(sum(arr[i:i+M]))
    print('#{} {}'.format(TC, max(sums)-min(sums)))
