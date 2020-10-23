import sys; sys.stdin = open('2005_input.txt', 'r')


def pascal(k):
    if k <= 2:
        return
    for i in range(k):
        if i == 0 or i == k-1:
            arr[k].append(1)
        else:
            arr[k].insert(i, arr[k-1][i-1]+arr[k-1][i])


for TC in range(1, int(input())+1):
    N = int(input())
    arr = [[] for _ in range(N+2)]
    arr[1].append(1)
    arr[2].append(1)
    arr[2].append(1)
    for i in range(1, N+1):
        pascal(i)

    print('#{}'.format(TC))
    for i in range(1, len(arr)-1):
        print(*arr[i])
