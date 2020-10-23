import sys; sys.stdin = open('4828_input.txt', 'r')

for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    MAX, MIN = max(arr), min(arr)
    print('#{} {}'.format(TC, MAX-MIN))
