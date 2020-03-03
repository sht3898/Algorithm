import sys; sys.stdin = open('4839_input.txt', 'r')


def search(low, high, target, cnt):
    c = (low + high) // 2
    if c == target:
        return cnt
    if c > target:
        cnt += 1
        return search(low, c, target, cnt+1)
    elif c < target:
        cnt += 1
        return search(c, high, target, cnt+1)


for TC in range(1, int(input())+1):
    P, A, B = map(int, input().split())
    a = search(1, P, A, 0)
    b = search(1, P, B, 0)
    if a > b:
        result = 'B'
    elif a < b:
        result = 'A'
    else:
        result = 0
    print('#{} {}'.format(TC, result))
